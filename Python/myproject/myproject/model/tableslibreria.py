from sqlalchemy import Table, ForeignKey, Column, Integer, Unicode, DateTime, Numeric, LargeBinary
from myproject.model import DeclarativeBase, metadata
from sqlalchemy.orm import relation,backref,relationship
from sqlalchemy import ForeignKey
from datetime import datetime

prestamo_books_table = Table('prestamo_books', metadata,
                        Column('usuario_id', Integer,
                               ForeignKey('usuarios.usuario_id',
                                          onupdate="CASCADE",
                                          ondelete="CASCADE"),
                               primary_key=True),
                        Column('book_id', Integer,
                               ForeignKey('books.book_id',
                                          onupdate="CASCADE",
                                          ondelete="CASCADE"),
                               primary_key=True))

class Usuario(DeclarativeBase):
   __tablename__ = 'usuarios'

   usuario_id = Column(Integer, primary_key=True)
   name = Column(Unicode(30))
   age = Column(Integer)
   phone = Column(Unicode(20))
   email_address = Column(Unicode(255), unique=True, nullable=False)
   created = Column(DateTime, default=datetime.now)
   image = Column(LargeBinary(length=(2 ** 32) - 1))
   book = relation('Book', secondary=prestamo_books_table, backref='usuarios')

   def __unicode__(self):
        return self.usuario_name

class Author(DeclarativeBase):
   __tablename__ = 'authors'

   author_id = Column(Integer, primary_key=True)
   name = Column(Unicode(30))
   created = Column(DateTime, default=datetime.now)
   book = relationship('Book', cascade="all,delete", backref='authors')

class Book(DeclarativeBase):
   __tablename__ = 'books'

   book_id = Column(Integer, primary_key=True)
   book_name = Column(Unicode(30))
   publication_date = Column(DateTime, default = None)
   created = Column(DateTime, default=datetime.now)
   author_id = Column(Integer, ForeignKey('authors.author_id'))
   usuario = relation('Usuario', secondary=prestamo_books_table, backref='books')

   def __unicode__(self):
        return self.book_name
