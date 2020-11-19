from pyramid.config import Configurator

from clld_glottologfamily_plugin import util
from clld_glottologfamily_plugin.util import ISOLATES_ICON

from clld.interfaces import IMapMarker, IValueSet, IValue, IDomainElement, ILanguage
from clldutils.svg import pie, icon, data_url

# we must make sure custom models are known at database initialization!
from tular import models


_ = lambda s: s
_('Contribution')
_('Contributions')
_('Parameter')
_('Parameters')


def url(spec):
    return data_url(icon(spec, opacity=0.9))


class LanguageByFamilyMapMarker(util.LanguageByFamilyMapMarker):
    def __call__(self, ctx, req):
        if IDomainElement.providedBy(ctx):
            return url('c' + ctx.jsondata['color'])

        if IValue.providedBy(ctx):
            if ctx.domainelement:
                return url('c' + ctx.domainelement.jsondata['color'])
            if ctx.valueset.language.jsondata['icon']:
                return url(ctx.valueset.language.jsondata['icon'])

        if IValueSet.providedBy(ctx):
            if ctx.values[0].domainelement:
                return url('c' + ctx.values[0].domainelement.jsondata['color'])
            if ctx.language.jsondata['icon']:
                return url(ctx.language.jsondata['icon'])
            if ctx.language.family:
                return url(ctx.language.family.jsondata['icon'])
            return url(req.registry.settings.get('clld.isolates_icon', ISOLATES_ICON))

        if ILanguage.providedBy(ctx):
            icon_ = super(LanguageByFamilyMapMarker, self).get_icon(ctx, req)
            if ctx.jsondata['icon']:
                icon_ = ctx.jsondata['icon']
            return url(icon_)

        return super(LanguageByFamilyMapMarker, self).__call__(ctx, req)



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('clld.web.app')

    config.include('clldmpg')
    config.include('clld_cognacy_plugin')
    config.include('clld_glottologfamily_plugin')
    config.add_route('completeness', '/completeness')
    home_comp = config.registry.settings['home_comp']
    home_comp.append('completeness')

    config.registry.registerUtility(LanguageByFamilyMapMarker(), IMapMarker)
    return config.make_wsgi_app()
