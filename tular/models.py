from zope.interface import implementer
from sqlalchemy import (
    Column,
    Unicode,
    Integer,
    ForeignKey,
)
import conllu

from clld import interfaces
from clld.db.meta import Base, CustomModelMixin, DBSession
from clld.db.models.common import Language, Parameter, ValueSet, Value, Sentence, Contribution
from clld_ipachart_plugin.models import InventoryMixin, Segment
from clld_glottologfamily_plugin.models import HasFamilyMixin

#-----------------------------------------------------------------------------
# specialized common mapper classes
#-----------------------------------------------------------------------------
@implementer(interfaces.ILanguage)
class Doculect(CustomModelMixin, Language, HasFamilyMixin, InventoryMixin):
    """
    From Language this model inherits: id, name, latitude (float), longitude
    (float).
    """
    pk = Column(Integer, ForeignKey('language.pk'), primary_key=True)
    subfamily = Column(Unicode)
    iso_code = Column(Unicode)
    glotto_code = Column(Unicode)

    @property
    def has_treebank(self):
        return bool(DBSession.query(Sentence).filter(Sentence.language_pk == self.pk).first())

    def treebank_url(self, req):
        if self.has_treebank:
            return req.route_url('sentences', _query=dict(language=self.id))

    def make_segment(self, sound_bipa, sound_name, request=None, **_):
        return Segment(
            sound_bipa=sound_bipa,
            sound_name=sound_name or '',
            href='https://clts.clld.org/parameters/{}'.format(sound_name.replace(' ', '_'))
                if sound_name else None)


@implementer(interfaces.IParameter)
class Concept(CustomModelMixin, Parameter):
    """
    From Parameter this model inherits: id, name.
    """
    pk = Column(Integer, ForeignKey('parameter.pk'), primary_key=True)
    portuguese = Column(Unicode)
    semantic_field = Column(Unicode)
    concepticon_class = Column(Unicode)
    eol = Column(Unicode)


@implementer(interfaces.IValue)
class Word(CustomModelMixin, Value):
    """
    Relevant fields inherited from Value: id, name, valueset.
    """
    pk = Column(Integer, ForeignKey('value.pk'), primary_key=True)
    simple_cognate = Column(Integer)
    partial_cognate = Column(Unicode)
    notes = Column(Unicode)
    morphemes = Column(Unicode)
    tokens = Column(Unicode)


@implementer(interfaces.ISentence)
class Example(CustomModelMixin, Sentence):
    """
    Relevant fields inherited from Value: id, name, valueset.
    """
    pk = Column(Integer, ForeignKey('sentence.pk'), primary_key=True)
    conllu = Column(Unicode)

    @property
    def tokenlist(self):
        return conllu.parse(self.conllu)[0]


@implementer(interfaces.IContribution)
class Database(CustomModelMixin, Contribution):
    pk = Column(Integer, ForeignKey('contribution.pk'), primary_key=True)
    doi = Column(Unicode)
