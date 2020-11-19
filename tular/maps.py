from clld.web.maps import Legend, Map
from clld.web.util.helpers import map_marker_img
from clld.web.util.htmllib import HTML
from clld.db.meta import DBSession

from tular import models


class LanguagesMap(Map):
    def get_options(self):
        return {'max_zoom': 12, 'base_layer': 'Esri.WorldImagery'}

    def get_legends(self):
        items = []
        seen = set()

        def item(lang, label):
            return HTML.div(map_marker_img(self.req, lang), ' ', label, style="padding-left: 5px")

        for lang in DBSession.query(models.Doculect).order_by(models.Doculect.subfamily):
            if lang.subfamily not in seen:
                items.append(item(lang, lang.subfamily))
                seen.add(lang.subfamily)
        yield Legend(self, 'subfamilies', items, label='Legend', stay_open=True)

        for legend in Map.get_legends(self):
            yield legend


def includeme(config):
    config.register_map('languages', LanguagesMap)
