from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql.types import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base


########################################################################################################################
# Manually Added for safrs, TODO: improve this crap
#
from safrs import SAFRSBase

Base = db.Model
metadata = Base.metadata

def BIGINT(_):
    return db.SMALLINT

def SMALLINT(_):
    return db.SMALLINT

def INTEGER(_):
    return db.INTEGER

def TIME(**kwargs):
    return db.TIME

TIMESTAMP= db.TIMESTAMP
NullType = db.String

########################################################################################################################



class Protagonist(SAFRSBase, Base):
    __tablename__ = 'protagonist'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum('person', 'company'))
    name = Column(Text, nullable=False)
    link = Column(Text)
    photo = Column(Text)
    dateUpdate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    quote = relationship('Quote', secondary='quoteAuthor')
    reference = relationship('Reference', secondary='referenceAuthor')


class QuoteLinkType(SAFRSBase, Base):
    __tablename__ = 'quoteLinkType'

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)


class QuoteType(SAFRSBase, Base):
    __tablename__ = 'quoteType'

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)


class ReferenceType(SAFRSBase, Base):
    __tablename__ = 'referenceType'

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)


class Theme(SAFRSBase, Base):
    __tablename__ = 'theme'

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)


class Company(SAFRSBase, Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, index=True)
    protagonistID = Column(ForeignKey('protagonist.id'), nullable=False, index=True)
    siret = Column(Text)
    dateUpdate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    protagonist = relationship('Protagonist')


class Person(SAFRSBase, Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True)
    protagonistID = Column(ForeignKey('protagonist.id'), nullable=False, index=True)
    surname = Column(Text)
    role = Column(Text)
    dateUpdate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    protagonist = relationship('Protagonist')


class Quote(SAFRSBase, Base):
    __tablename__ = 'quote'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    details = Column(LONGTEXT)
    typeID = Column(ForeignKey('quoteType.id'), nullable=False, index=True)
    dateUpdate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    quoteType = relationship('QuoteType')
    reference = relationship('Reference', secondary='quoteReference')
    theme = relationship('Theme', secondary='quoteTheme')


class Reference(SAFRSBase, Base):
    __tablename__ = 'reference'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    details = Column(LONGTEXT)
    url = Column(LONGTEXT)
    date = Column(Date)
    typeID = Column(ForeignKey('referenceType.id'), nullable=False, index=True)
    reliability = Column(Integer)
    dateUpdate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    referenceType = relationship('ReferenceType')


t_quoteAuthor = Table(
    'quoteAuthor', metadata,
    Column('quoteID', ForeignKey('quote.id'), nullable=False, index=True),
    Column('authorID', ForeignKey('protagonist.id'), nullable=False, index=True)
)


t_quoteLink = Table(
    'quoteLink', metadata,
    Column('quoteMainID', ForeignKey('quote.id'), nullable=False, index=True),
    Column('quoteSupportID', ForeignKey('quote.id'), nullable=False, index=True),
    Column('typeID', ForeignKey('quoteLinkType.id'), nullable=False, index=True),
    Column('dateUpdate', DateTime, server_default=text("CURRENT_TIMESTAMP"))
)


t_quoteReference = Table(
    'quoteReference', metadata,
    Column('quoteID', ForeignKey('quote.id'), nullable=False, index=True),
    Column('referenceID', ForeignKey('reference.id'), nullable=False, index=True)
)


t_quoteTheme = Table(
    'quoteTheme', metadata,
    Column('themeID', ForeignKey('theme.id'), nullable=False, index=True),
    Column('quoteID', ForeignKey('quote.id'), nullable=False, index=True)
)


t_referenceAuthor = Table(
    'referenceAuthor', metadata,
    Column('referenceID', ForeignKey('reference.id'), nullable=False, index=True),
    Column('authorID', ForeignKey('protagonist.id'), nullable=False, index=True)
)

