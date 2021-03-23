import pathlib
import itertools
import collections

from clldutils.misc import slug
from clldutils.markup import iter_markdown_tables
from clldutils import jsonlib
from clld.cliutil import Data, bibtex2source
from clld.db.meta import DBSession
from clld.db.models import common
from clld.db.util import compute_language_sources
from clld.lib import bibtex
from pycldf import Dataset
from nameparser import HumanName
from clld_cognacy_plugin.models import Cognate, Cognateset
from clld_glottologfamily_plugin.models import Family
from pyclts import CLTS

import tular
from tular.models import Doculect, Word, Concept, Example, Database

SUBGROUPS = {
    'nonTupían': 'd222255',
    'Arikem': 'cbbccee',
    'Aweti': 'ccceeff',
    'Juruna': 'cccddaa',
    'Mawé': 'ceeeebb',
    'Mondé': 'cffcccc',
    'Munduruku': 'cdddddd',
    'Ramarana-Purubora': 'c225555',
    'Tuparí': 'c666633',
    'Tupi-Guarani': 'c663333',
    'Omagua-Kokama': 'c336633',
}
DATASETS = collections.OrderedDict([
    ('tuled', 'https://doi.org/10.5281/zenodo.4629306'),
    ('tudet', None),
])


def add_sources(sources_file_path, session):
    bibtex_db = bibtex.Database.from_file(sources_file_path, encoding='utf-8')
    for record in bibtex_db:
        session.add(bibtex2source(record))
        yield record.id
    session.flush()


def main(args):
    data = Data()
    dataset = data.add(
        common.Dataset, 'tular',
        id=tular.__name__,
        domain="tular.clld.org",
        name="TuLaR",
        description="Tupían Language Resources",
        publisher_name="Max-Planck Institute for Evolutionary Anthropology",
        publisher_place="Leipzig",
        license='https://creativecommons.org/licenses/by-sa/4.0/',
        contact="team@tuled.org",
        jsondata={
            'license_icon': 'cc-by-sa.png',
            'license_name': 'Creative Commons Attribution-ShareAlike 4.0 International License'},
    )

    rd = pathlib.Path(tular.__file__).parent.parent.parent.resolve()
    root = input('Project dir [{}]: '.format(str(rd)))
    root = pathlib.Path(root) if root else rd
    clts_dir = rd / '..' / 'cldf-clts' / 'clts-data'
    clts = CLTS(input('Path to cldf-clts/clts [{}]: '.format(str(clts_dir))) or clts_dir)

    for db, doi in DATASETS.items():
        dbdir = root.joinpath(db)
        assert dbdir.exists()
        md = jsonlib.load(dbdir / 'metadata.json')
        contribution = data.add(
            Database, db,
            id=db,
            name=md['title'],
            description=md['description'],
            doi=doi,
        )
        header, contribs = next(iter_markdown_tables(
            dbdir.joinpath('CONTRIBUTORS.md').read_text(encoding='utf8')))
        for i, contrib in enumerate(contribs):
            contrib = dict(zip(header, contrib))
            cid = slug(HumanName(contrib['Name']).last)
            contributor = data['Contributor'].get(cid)
            if not contributor:
                contributor = data.add(common.Contributor, cid, id=cid, name=contrib['Name'])
            DBSession.add(common.ContributionContributor(
                contribution=contribution,
                contributor=contributor,
                ord=i,
            ))

    for i, cid in enumerate(['gerardi', 'reichert', 'aragon', 'list', 'forkel']):
        DBSession.add(common.Editor(
            contributor=data['Contributor'][cid], dataset=dataset, ord=i))

    source_ids = list(add_sources(args.cldf.bibpath, DBSession))
    sources = {s.id: s.pk for s in DBSession.query(common.Source)}
    subgroups = []

    for row in args.cldf['LanguageTable']:
        if row['SubGroup'] not in subgroups:
            subgroups.append(row['SubGroup'])
        family = data['Family'].get(row['Family'])
        if (not family) and row['Family']:
            family = data.add(Family, row['Family'], id=slug(row['Family']), name=row['Family'])
        data.add(
            Doculect,
            row['ID'],
            id=row['ID'],
            name=row['Name'].replace('_', ' '),
            family=family,
            subfamily=row['SubGroup'],
            iso_code=row['ISO639P3code'],
            glotto_code=row['Glottocode'],
            longitude=row['Longitude'],
            latitude=row['Latitude'],
            jsondata=dict(icon=SUBGROUPS[row['SubGroup']]),
        )

    tudet = Dataset.from_metadata(root / 'tudet' / 'cldf' / 'Generic-metadata.json')
    seen = set()
    for row in tudet['ExampleTable']:
        if row['ID'] in seen:
            print('skipping duplicate sentence ID {}'.format(row['ID']))
            continue
        seen.add(row['ID'])
        DBSession.add(Example(
            id=row['ID'],
            name=row['Primary_Text'],
            description=row['Translated_Text'],
            language=data['Doculect'][row['Language_ID']],
            conllu=row['conllu']))

    contrib = data['Database']['tuled']
    for row in args.cldf['ParameterTable']:
        data.add(
            Concept,
            row['ID'],
            id=row['ID'].split('_')[0],
            name=row['Name'],
            portuguese=row['Portuguese_Gloss'],
            semantic_field=row['Semantic_Field'],
            concepticon_class=row['Concepticon_ID'],
            eol=row['EOL_ID'],
        )
    inventories = collections.defaultdict(set)
    for (lid, pid), rows in itertools.groupby(
        sorted(args.cldf.iter_rows('FormTable', 'languageReference', 'parameterReference'),
               key=lambda r: (r['Language_ID'], r['Parameter_ID'])),
        lambda r: (r['Language_ID'], r['Parameter_ID']),
    ):
        vsid = '{}-{}'.format(lid, pid)
        vs = data.add(
            common.ValueSet, vsid,
            id=vsid,
            language=data['Doculect'][lid],
            parameter=data['Concept'][pid],
            contribution=contrib,
        )
        refs = set()
        for row in rows:
            inventories[row['languageReference']] = inventories[row['languageReference']].union(
                row['Segments'])
            data.add(
                Word,
                row['ID'],
                id=row['ID'],
                valueset=vs,
                name=row['Form'],
                tokens=' '.join(row['Segments']),
                simple_cognate=int(row['SimpleCognate']),
                notes=row['Comment'],
                morphemes=' '.join(row['Morphemes']),
                partial_cognate=' '.join([k for k in row['PartialCognates']]) if row['PartialCognates'] else None,
            )
            refs = refs.union(row['Source'])

        for ref in refs:
            if ref in source_ids:
                DBSession.add(common.ValueSetReference(valueset=vs, source_pk=sources[slug(ref, lowercase=False)]))

    for lid, inv in inventories.items():
        inv = [clts.bipa[c] for c in inv]
        data['Doculect'][lid].update_jsondata(
            inventory=[(str(c), c.name) for c in inv if hasattr(c, 'name')])

    for row in args.cldf['CognateTable']:
        cc = data['Cognateset'].get(row['Cognateset_ID'])
        if not cc:
            cc = data.add(
                Cognateset,
                row['Cognateset_ID'],
                id=row['Cognateset_ID'],
                name=row['Cognateset_ID'],
                contribution=contrib,
            )
        data.add(
            Cognate,
            row['ID'],
            cognateset=cc,
            counterpart=data['Word'][row['Form_ID']],
            alignment=' '.join(row['Alignment'] or []),
        )

    #load_families(
    #    Data(),
    #    [(l.glotto_code, l) for l in data['Doculect'].values()],
    #    glottolog_repos=args.glottolog,
    #    isolates_icon='tcccccc',
    #    strict=False,
    #)


def prime_cache(args):
    """If data needs to be denormalized for lookup, do that here.
    This procedure should be separate from the db initialization, because
    it will have to be run periodically whenever data has been updated.
    """
    compute_language_sources()
