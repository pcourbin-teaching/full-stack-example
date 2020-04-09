# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, Table, Text, text, create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

#https://github.com/zalando/connexion/tree/master/examples/openapi3/sqlalchemy





def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session

class ProtagonistDB(Base):
    __tablename__ = 'protagonist'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(u'person', u'company'))
    name = Column(Text, nullable=False)
    link = Column(Text)
    photo = Column(Text)
    dateUpdate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    quote = relationship(u'QuoteDB', secondary=u'quoteAuthor')
    reference = relationship(u'ReferenceDB', secondary=u'referenceAuthor')


class CompanyDB(ProtagonistDB):
    __tablename__ = 'company'

    id = Column(ForeignKey(u'protagonist.id'), primary_key=True, index=True)
    siret = Column(Text)
    dateUpdate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))


class PersonDB(ProtagonistDB):
    __tablename__ = 'person'

    id = Column(ForeignKey(u'protagonist.id'), primary_key=True, index=True)
    surname = Column(Text)
    role = Column(Text)
    dateUpdate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))


class QuoteLinkTypeDB(Base):
    __tablename__ = 'quoteLinkType'

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)


class QuoteTypeDB(Base):
    __tablename__ = 'quoteType'

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)


class ReferenceTypeDB(Base):
    __tablename__ = 'referenceType'

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)


class ThemeDB(Base):
    __tablename__ = 'theme'

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)

    def update(self, id=None, title=None):
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class QuoteDB(Base):
    __tablename__ = 'quote'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    details = Column(LONGTEXT)
    typeID = Column(ForeignKey(u'quoteType.id'), nullable=False, index=True)
    dateUpdate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    quoteType = relationship(u'QuoteTypeDB')
    theme = relationship(u'ThemeDB', secondary=u'quoteTheme')
    reference = relationship(u'ReferenceDB', secondary=u'quoteReference')


    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


class ReferenceDB(Base):
    __tablename__ = 'reference'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    details = Column(LONGTEXT)
    url = Column(LONGTEXT)
    date = Column(Date)
    typeID = Column(ForeignKey(u'referenceType.id'), nullable=False, index=True)
    reliability = Column(Integer)
    dateUpdate = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    referenceType = relationship(u'ReferenceTypeDB')

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


t_quoteAuthor = Table(
    'quoteAuthor', metadata,
    Column('quoteID', ForeignKey(u'quote.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True),
    Column('authorID', ForeignKey(u'protagonist.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
)


t_quoteLink = Table(
    'quoteLink', metadata,
    Column('quoteMainID', ForeignKey(u'quote.id'), nullable=False, index=True),
    Column('quoteSupportID', ForeignKey(u'quote.id'), nullable=False, index=True),
    Column('typeID', ForeignKey(u'quoteLinkType.id'), nullable=False, index=True),
    Column('dateUpdate', DateTime, server_default=text("CURRENT_TIMESTAMP"))
)


t_quoteReference = Table(
    'quoteReference', metadata,
    Column('quoteID', ForeignKey(u'quote.id'), nullable=False, index=True),
    Column('referenceID', ForeignKey(u'reference.id'), nullable=False, index=True)
)


t_quoteTheme = Table(
    'quoteTheme', metadata,
    Column('themeID', ForeignKey(u'theme.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True),
    Column('quoteID', ForeignKey(u'quote.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
)


t_referenceAuthor = Table(
    'referenceAuthor', metadata,
    Column('referenceID', ForeignKey(u'reference.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True),
    Column('authorID', ForeignKey(u'protagonist.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
)
