from clld.web import datatables
from clld.web.datatables.base import LinkCol, Col, LinkToMapCol
from clld.web.datatables.contribution import Contributions, ContributorsCol
from clld.web.util.helpers import map_marker_img, link
from clld.web.util.htmllib import HTML
from clld.db.util import get_distinct_values
from clld.db.models import common

from tular import models


class SubGroupCol(Col):
    def format(self, item):
        return HTML.div(map_marker_img(self.dt.req, item), ' ', item.subfamily)


class DoculectLinkCol(LinkCol):
    def format(self, item):
        item = self.get_obj(item)
        return HTML.div(
            map_marker_img(self.dt.req, item),
            ' ',
            link(self.dt.req, item))


class Languages(datatables.Languages):
    def col_defs(self):
        return [
            LinkToMapCol(self, 'm'),
            LinkCol(self, 'name'),
            SubGroupCol(
                self,
                'subfamily',
                choices=get_distinct_values(models.Doculect.subfamily),
                model_col=models.Doculect.subfamily),
            Col(self, 'glottocode', model_col=models.Doculect.glotto_code),
            Col(self, 'isocode', sTitle='ISO Code', model_col=models.Doculect.iso_code),
            Col(self,
                'latitude',
                sDescription='<small>The geographic latitude</small>'),
            Col(self,
                'longitude',
                sDescription='<small>The geographic longitude</small>'),
        ]


class PartialCognatesCol(Col):
    def format(self, item):
        parts = []
        for i, cogid in enumerate((item.partial_cognate or '').split()):
            if i > 0:
                parts.append('+')
            parts.append(HTML.a(cogid, href=self.dt.req.route_url('cognateset', id=cogid)))

        return HTML.span(*parts)


class Words(datatables.Values):

    def col_defs(self):
        res = []

        if self.language:
            res.extend([
                LinkCol(self, 'concept', get_object=lambda i: i.valueset.parameter, model_col=common.Parameter.name),
                #IntegerIdCol(self, 'id', model_col=Concept.id,
                #    get_object=lambda x: x.valueset.parameter),
                #ConceptLinkCol(self, 'concept', model_col=Concept.name,
                #    get_object=lambda x: x.valueset.parameter)
            ])

        elif self.parameter:
            res.extend([
                DoculectLinkCol(self, 'language', model_col=models.Doculect.name,
                    get_object=lambda x: x.valueset.language) ])

        res.extend([
            Col(self, 'form', model_col=models.Word.name, sTitle='Orthographic form'),
            Col(self, 'tokens', model_col=models.Word.tokens, sTitle='Tokens'),
            Col(self, 'simple_cognate', input_size='mini', model_col=models.Word.simple_cognate, sTitle='Simple Cognate'),
            PartialCognatesCol(self, 'partial_cognate', model_col=models.Word.partial_cognate, sTitle='Partial Cognate'),
            Col(self, 'notes', model_col=models.Word.notes, sTitle='Notes'),
            Col(self, 'morphemes', model_col=models.Word.morphemes, sTitle='Morphemes')]
        )

        return res


class Databases(Contributions):
    def col_defs(self):
        return [
            LinkCol(self, 'name'),
            Col(self, 'description'),
            ContributorsCol(self, 'contributor'),
        ]


def includeme(config):
    config.register_datatable('languages', Languages)
    config.register_datatable('values', Words)
    config.register_datatable('contributions', Databases)
