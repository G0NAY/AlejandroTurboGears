from sqlalchemy import Table, ForeignKey, Column, Integer, Unicode, DateTime, Numeric
from myproject.model import DeclarativeBase, metadata
from sqlalchemy.orm import relation,backref,relationship
from sqlalchemy import ForeignKey
from datetime import datetime


class Tracker(DeclarativeBase):
    __tablename__ = 'tracker'
    id = Column(Integer, primary_key=True)
    imei = Column(Unicode(16))
    ticket = Column(Integer)
    name = Column(Unicode(50))

class PhoneBook(DeclarativeBase):
    __tablename__ = 'phonebook'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(30))
    birthday = Column(DateTime, default=datetime.now)
    age = Column(Integer)
    phone = Column(Unicode(20))
    loans = relationship('Loans', cascade="all,delete", backref='phonebook')

class Loans(DeclarativeBase):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True)
    amount = Column(Numeric(8, 2), default=0)
    due_date = Column(DateTime, default=datetime.now)
    phonebook_id = Column(Integer, ForeignKey('phonebook.id'))

class Distribuciones(DeclarativeBase):
    __tablename__ = 'distribuciones'
    id = Column(Integer, primary_key=True)
    imei = Column(Unicode(16))
    ticket = Column(Integer)
    name = Column(Unicode(50))



'''
#-----------------------
subcategory_stages_table = Table('subcategory_stages', metadata,
                                 Column('subcategory_id', Integer, ForeignKey('subcategories.subcategory_id')),
                                 Column('stage_id', Integer, ForeignKey('stages.stage_id'))
                                 )


class Subcategory(DeclarativeBase):
    _tablename_ = 'subcategories'
    subcategory_id = Column(Integer, primary_key=True)
    subcategory_name = Column(Unicode(40), nullable=False)

    stage = relation("Stage", secondary=subcategory_stages_table, backref='subcategories')

    def __unicode__(self):
        return self.subcategory_name


class Stage(DeclarativeBase):
    _tablename_ = 'stages'
    stage_id = Column(Integer, primary_key=True)
    stage_name = Column(Unicode(40), nullable=False)

    subcategory = relation("Subcategory", secondary=subcategory_stages_table, backref='stages')

    def __unicode__(self):
        return self.stage_name
'''



