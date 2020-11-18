from zope.interface import implementer
from sqlalchemy import (
    Column,
    String,
    Unicode,
    Integer,
    Boolean,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_property
import conllu

from clld import interfaces
from clld.db.meta import Base, CustomModelMixin
from clld.db.models.common import Language, Parameter, ValueSet, Value, Sentence
from clld_cognacy_plugin.models import Cognate

#-----------------------------------------------------------------------------
# specialized common mapper classes
#-----------------------------------------------------------------------------
#@implementer(interfaces.ILanguage)
#class tuledLanguage(CustomModelMixin, Language):
#    pk = Column(Integer, ForeignKey('language.pk'), primary_key=True)


@implementer(interfaces.ILanguage)
class Doculect(CustomModelMixin, Language):
    """
    From Language this model inherits: id, name, latitude (float), longitude
    (float).
    """
    pk = Column(Integer, ForeignKey('language.pk'), primary_key=True)
    subfamily = Column(Unicode)
    iso_code = Column(Unicode)
    glotto_code = Column(Unicode)


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
    partial_cognate = Column(Integer)
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
