from sqlalchemy import func
from clld.db.models import common
from clld.db.meta import DBSession
from clld.web.util import glottolog


def glottolog_link(req, lang):
    if lang.glottocode:
        return glottolog.link(req, lang.glottocode, label=lang.glottocode)
    return ''


def fix_conllu(s):
    fixed = []
    for line in s.split('\n'):
        if not line.startswith('#'):
            parts = line.split('\t')
            if len(parts) >= 8:
                print(parts)
                if parts[8] == '{}:{}'.format(parts[6], parts[7]):
                    parts[8] = '_'
                    print(parts)
                    line = '\t'.join(parts)
        fixed.append(line)
    return '\n'.join(fixed)


def sentence_index_html(context=None, request=None, **kw):
    if request.params.get('language'):
        lang = common.Language.get(request.params['language'])
        return dict(
            lang=lang,
            sentences=DBSession.query(common.Sentence)
                    .filter(common.Sentence.language_pk == lang.pk).all())
    return dict(lang=None, sentences=[])


def contribution_detail_html(context=None, request=None, **kw):
    if context.id == 'tudet':
        langs = DBSession.query(common.Language).join(common.Sentence).distinct()
        counts = DBSession.query(common.Sentence.language_pk, func.count(common.Sentence.pk))\
            .group_by(common.Sentence.language_pk).all()
        counts = dict(counts)
        return dict(languages=[(l, counts[l.pk]) for l in sorted(langs, key=lambda l: l.name)])
    return {}
