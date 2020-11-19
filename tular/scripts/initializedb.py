import itertools

from clldutils.misc import slug
from clld.cliutil import Data, bibtex2source
from clld.db.meta import DBSession
from clld.db.models import common
from clld.db.util import compute_language_sources
from clld.lib import bibtex
from pycldf import Dataset
from clld_cognacy_plugin.models import Cognate, Cognateset
from clld_glottologfamily_plugin.util import load_families

import tular
from tular.models import Doculect, Word, Concept, Example
from .metadata import CONTRIBUTORS

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
}


def add_meta_data(session, data):
    """
    Creates and adds to the given SQLAlchemy session the common.Dataset and
    related model instances that comprise the project's meta info.
    Helper for the main function that keeps the meta data in one place for
    easier reference and editing.
    """

    dataset = common.Dataset(
        id=tular.__name__,
        domain="tular.clld.org",
        name="TuLaR",
        description="Tupían Language Resources",
        publisher_name="Seminar für Sprachwissenschaft at the University of Tübingen",
        publisher_place="Tübingen",
        license='https://creativecommons.org/licenses/by-sa/4.0/',
        contact="team@tuled.org",
        jsondata={
            'license_icon': 'cc-by-sa.png',
            'license_name': 'Creative Commons Attribution-ShareAlike 4.0 International License'},
    )

    for cid, name in CONTRIBUTORS.items():
        data.add(common.Contributor, cid, id=cid, name=name)
    for i, cid in enumerate(['gerardi', 'reichert', 'aragon']):
        DBSession.add(common.Editor(dataset=dataset, contributor=data['Contributor'][cid], ord=i))

    session.add(dataset)


def add_sources(sources_file_path, session):
    """
    Creates and adds to the given SQLAlchemy session the common.Source model
    instances that comprise the project's references. Expects the path to a
    bibtex file as its first argument.
    Returns a dict containing the added model instances with the bibtex IDs
    being the keys.
    Helper for the main function.
    """
    bibtex_db = bibtex.Database.from_file(sources_file_path, encoding='utf-8')
    for record in bibtex_db:
        session.add(bibtex2source(record))
        yield record.id
    session.flush()


def main(args):
    data = Data()
    add_meta_data(DBSession, data)
    contrib = data.add(common.Contribution, 'tuled', id='tuled', name='tuled')
    for i, cid in enumerate(['gerardi', 'reichert', 'aragon', 'list', 'wientzek']):
        DBSession.add(common.ContributionContributor(
            contribution=contrib,
            contributor=data['Contributor'][cid],
            ord=i,
        ))

    source_ids = list(add_sources(args.cldf.bibpath, DBSession))
    sources = {s.id: s.pk for s in DBSession.query(common.Source)}
    subgroups = []
    for row in args.cldf['LanguageTable']:
        if row['SubGroup'] not in subgroups:
            subgroups.append(row['SubGroup'])
        data.add(
            Doculect,
            row['ID'],
            id=row['ID'],
            name=row['Name'].replace('_', ' '),
            subfamily=row['SubGroup'],
            iso_code=row['ISO639P3code'],
            glotto_code=row['Glottocode'],
            longitude=row['Longitude'],
            latitude=row['Latitude'],
            jsondata=dict(icon=SUBGROUPS.get(row['SubGroup'])),
        )

    tudet = Dataset.from_metadata(args.cldf.directory.parent.parent / 'tudet' / 'cldf' / 'Generic-metadata.json')
    for row in tudet['ExampleTable']:
        DBSession.add(Example(
            id=row['ID'],
            name=row['Primary_Text'],
            description=row['Translated_Text'],
            language=data['Doculect'][row['Language_ID']],
            conllu=row['conllu']))
    #return

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
    for (lid, pid), rows in itertools.groupby(
        sorted(args.cldf['FormTable'], key=lambda r: (r['Language_ID'], r['Parameter_ID'])),
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

    load_families(
        Data(),
        [(l.glotto_code, l) for l in data['Doculect'].values()],
        glottolog_repos=args.glottolog,
        isolates_icon='tcccccc',
        strict=False,
    )


def prime_cache(args):
    """If data needs to be denormalized for lookup, do that here.
    This procedure should be separate from the db initialization, because
    it will have to be run periodically whenever data has been updated.
    """
    compute_language_sources()
