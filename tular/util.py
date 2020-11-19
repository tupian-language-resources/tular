from clld.web.util import glottolog


def glottolog_link(req, lang):
    if lang.glottocode:
        return glottolog.link(req, lang.glottocode, label=lang.glottocode)
    return ''
