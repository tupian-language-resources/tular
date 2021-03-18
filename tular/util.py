from sqlalchemy import func
from clld.db.models import common
from clld.db.meta import DBSession
from clld.web.util import glottolog

from clld.web.util.helpers import link


def glottolog_link(req, lang):
    if lang.glottocode:
        return glottolog.link(req, lang.glottocode, label=lang.glottocode)
    return ''


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
        return dict(languages=[(l, counts[l.pk]) for l in langs])
    return {}
