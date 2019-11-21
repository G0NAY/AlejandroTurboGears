# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from myproject import model
from myproject.controllers.secure import SecureController
from myproject.model import DBSession
import transaction
from myproject.model.auth import User, Group, Permission
from tg import render_template
from myproject.model.tables import Tracker, Distribuciones, PhoneBook, Loans
from myproject.model.tableslibreria import Usuario, Author, Book, prestamo_books_table
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
from myproject.controllers.jqgrid import jqgridDataGrabber

from myproject.lib.base import BaseController
from myproject.controllers.error import ErrorController
import requests

__all__ = ['LibreriaController']


class LibreriaController(BaseController):

    def __init___(self):
        pass

    @expose('myproject.templates.libreria.libreria')
    def libreria(self):
        return dict()

    @expose('json')
    def displayUsuarios(self, **kw):
        displayusuarios = render_template({"list": list}, "mako",'myproject.templates.libreria.displayusuarios')
        return dict(displayusuarios=displayusuarios)

    @expose('json')
    def displayBooks(self, **kw):
        displaybooks = render_template({"list": list}, "mako",'myproject.templates.libreria.displaybooks')
        return dict(displaybooks=displaybooks)

    @expose('json')
    def loadUsuario(self, **kw):
        filter = []
        return jqgridDataGrabber(Usuario, 'usuario_id', filter, kw).loadGrid()

    @expose('json')
    def updateUsuario(self, **kw):
        filter = []
        return jqgridDataGrabber(Usuario, 'usuario_id', filter, kw).updateGrid()

    @expose('json')
    def loadAuthor(self, **kw):
        filter = []
        return jqgridDataGrabber(Author, 'author_id', filter, kw).loadGrid()

    @expose('json')
    def updateAuthor(self, **kw):
        filter = []
        return jqgridDataGrabber(Author, 'author_id', filter, kw).updateGrid()

    @expose('json')
    def loadBook(self, **kw):
        filter = []
        return jqgridDataGrabber(Book, 'book_id', filter, kw).loadGrid()

    @expose('json')
    def updateBook(self, **kw):
        filter = []
        return jqgridDataGrabber(Book, 'book_id', filter, kw).updateGrid()

    @expose('json')
    def openClose(self, **kw):
        handler_user = DBSession.query(prestamo_books_table).filter_by(usuario_id=kw['id']).all()
        kw['usuario'] = DBSession.query(Usuario).filter_by(usuario_id=kw['id']).first()
        kw['book'] = []
        for item in handler_user:
            handler_book = DBSession.query(Book).filter_by(book_id=item.book_id).first()
            if handler_book != None:
                kw['book'].append({'book_name': handler_book.book_name})
        dialogtemplate = render_template(kw, "mako", 'myproject.templates.libreria.hello')
        return dict(dialogtemplate=dialogtemplate)

    @expose('myproject.templates.libreria.libreria')
    def tablaBase(self):
        return dict()

    @expose('myproject.templates.libreria.testbasededatos')
    def tablaBase2(self):
        return dict()

    @expose('json')
    def tablaBaseConec(self, **kw):
        prestamos = DBSession.query(prestamo_books_table).all()  # prestamos recibe todos los elementos de la tabla prestamos
        relacion = []  # Se crea una nueva lista donde almacenaremos datos
        for prestamo in prestamos:  # Recorremos los elementos de prestamos
            usuario = DBSession.query(Usuario).filter_by(usuario_id=prestamo.usuario_id).first()  # la variable usuario recibe elementos de la tabla Usuario donde usuario_id es igual a la misma posicion en prestamos
            libro = DBSession.query(Book).filter_by(book_id=prestamo.book_id).first()  # la variable libro recibe elementos de la tabla Book donde book_id es igual a la misma posicion en prestamos
            relacion.append({'usuario_id': usuario.name, 'book_id': libro.book_name})  # Se regresa a relacion cada posicion recorrida en prestamos y se envia el nombre de las tablas Book y Usuario
        return dict(total=200, page=1, records=500, rows=relacion)  # Regresamos un Json con formato total, page, records, rows que es como lo requiere nuestro jqgrid

    @expose('json')
    def prestamosTemplate(self, **kw):
        list = []
        prestamostemplate = render_template({"list": list}, "mako", 'myproject.templates.libreria.prestamostemplate')
        return dict(prestamostemplate=prestamostemplate)

    @expose('json')
    def alertPrestamo(self, **kw):
        usuario_id = kw["usuario_id"]
        book_id = kw["book_id"]
        error = "ok"
        books = []  # lista de libros
        usuario = DBSession.query(Usuario).filter_by(usuario_id=usuario_id).first()  # Busca el Usuario
        print(usuario)
        count = 0
        for item in usuario.book:  # Busca los libros que ya tiene el usuario asignado
            books.append(item)  # Agregalos a la lista
            count += 1
        if count < 3:
            if usuario != None:  # Si existe el usuario busca el libro
                book = DBSession.query(Book).filter_by(book_id=book_id).first()  # Busca el libro
                if book != None:  # Si existe el libro
                    if book not in books:  # Si el libro no lo tiene el usuario aun
                        books.append(book)  # Agrega el libro a la lista
                    else:
                        error = "Ya lo tiene asignado"
                usuario.book = books  # Agrega a la lista de libros al usuario
        else:
            error = "Ya tiene 3 libros asignados. No puede sacar más libros"
        return dict(book=book)
