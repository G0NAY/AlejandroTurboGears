# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from myproject import model
from myproject.controllers.secure import SecureController
from myproject.model import DBSession, User
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
from myproject.controllers.libreria.libreria import LibreriaController
from myproject.controllers.reload.reload import ReloadController
from myproject.controllers.courses.courses import CoursesController

__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the myproject application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    error = ErrorController()

    libreria = LibreriaController()
    reload = ReloadController()
    courses = CoursesController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "myproject"

    @expose('myproject.templates.index')
    def index(self,**kw):

        """Handle the front-page."""

        return dict(page='index')
    @expose('myproject.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('myproject.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(page='environ', environment=request.environ)

    @expose('myproject.templates.data')
    @expose('json')
    def data(self, **kw):
        """
        This method showcases how you can use the same controller
        for a data page and a display page.
        """
        return dict(page='data', params=kw)
    @expose('myproject.templates.index')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def manage_permission_only(self, **kw):
        """Illustrate how a page for managers only works."""
        return dict(page='managers stuff')

    @expose('myproject.templates.index')
    @require(predicates.is_user('editor', msg=l_('Only for the editor')))
    def editor_user_only(self, **kw):
        """Illustrate how a page exclusive for the editor works."""
        return dict(page='editor stuff')

    @expose('myproject.templates.login')
    def login(self, came_from=lurl('/'), failure=None, login=''):
        """Start the user login."""
        if failure is not None:
            if failure == 'user-not-found':
                flash(_('User not found'), 'error')
            elif failure == 'invalid-password':
                flash(_('Invalid Password'), 'error')

        login_counter = request.environ.get('repoze.who.logins', 0)
        if failure is None and login_counter > 0:
            flash(_('Wrong credentials'), 'warning')

        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from, login=login)

    @expose()
    def post_login(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                     params=dict(came_from=came_from, __logins=login_counter))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)

        # Do not use tg.redirect with tg.url as it will add the mountpoint
        # of the application twice.
        return HTTPFound(location=came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        return HTTPFound(location=came_from)

    @expose('myproject.templates.weather')
    def weather(self):
        url = "http://api.openweathermap.org/data/2.5/weather?id=3523272&appid=d0aa2d3106f2aa9e95523348582e2d6c&units=metric&lang=es"
        r = requests.get(url)
        json = r.json()
        temperature = json['main']['temp']
        pressure = json['main']['pressure']
        humidity = json['main']['humidity']
        return dict(temperature=temperature, pressure=pressure, humidity=humidity)

    @expose('myproject.templates.datosweather')
    def datosweather(self):
        url = "http://api.openweathermap.org/data/2.5/weather?id=3523272&appid=d0aa2d3106f2aa9e95523348582e2d6c&units=metric&lang=es"
        r = requests.get(url)
        json = r.json()
        return dict(json=json)

    @expose('myproject.templates.makoconnection.connection')
    def connection(self, **kw):
        tracker = DBSession.query(Tracker).all() #tracker recibe todos los elementos de la base de datos
        kw['tracker'] = [] #Declaramos una nueva lista dentro del diccionario kw que tiene por llave 'tracker'
        for item in tracker: #Iteramos cada elemento que este denro de trecker de la base de datos
            kw['tracker'].append({'id': item.id, 'imei': item.imei, 'ticket': item.ticket, 'name': item.name}) #agregr diccionarios a la lista kw 'tracker'
        return dict(page='connection', kw=kw)

    @expose('myproject.templates.makoconnection.test')
    def test(self):
        return dict()

    @expose('myproject.templates.makoconnection.telefonica')
    def telefonica(self):
        return dict()

    @expose('json')
    def loadjqgridtelefonica(self, **kw):
        for x, y in kw.items():
            print("{} {}".format(x, y))
        page = kw["page"]
        records = []
        print(page)
        if page == "1":
            totalPages = 2
            selectedpage = 1

            id = "1"
            icc = "2345897458759"
            lifecyclestatus = "life1"
            records.append({'id': id, 'cell': [id, icc, lifecyclestatus]})
            id = "2"
            icc = "3452345235545"
            lifecyclestatus = "life2"
            records.append({'id': id, 'cell': [id, icc, lifecyclestatus]})
            totalRecords = len(records)
            id = "3"
            icc = "323232323233223"
            lifecyclestatus = "life3"
            records.append({'id': id, 'cell': [id, icc, lifecyclestatus]})
            totalRecords = len(records)
            id = "4"
            icc = "2345897458759"
            lifecyclestatus = "life1"
            records.append({'id': id, 'cell': [id, icc, lifecyclestatus]})
            id = "5"
            icc = "3452345235545"
            lifecyclestatus = "life2"
            records.append({'id': id, 'cell': [id, icc, lifecyclestatus]})
            totalRecords = len(records)
        if page == "2":
            totalPages = 2
            selectedpage = 2
            id = "6"
            icc = "323232323233223"
            lifecyclestatus = "life3"
            records.append({'id': id, 'cell': [id, icc, lifecyclestatus]})
        totalRecords = len(records)
        return dict(total=totalPages, page=selectedpage, records=totalRecords, rows=records)


    @expose('myproject.templates.makoconnection.vistasj')
    def vistasj(self):
        return dict()

    @expose('json')
    def loadweather(self, **j):
        url = "http://api.openweathermap.org/data/2.5/weather?id=3523272&appid=d0aa2d3106f2aa9e95523348582e2d6c&units=metric&lang=es"
        r = requests.get(url)
        json = r.json()
        return dict(total= 200, page=1, records=500, rows = json['weather'])

    @expose('myproject.templates.makoconnection.vistasj2')
    def vistasj2(self):
        return dict()

    @expose('myproject.templates.jqgrid')
    def jqgrid(self):
        return dict()

    @expose('json')
    def loadTest2(self, **kw):
        filter = []
        return jqgridDataGrabber(Tracker, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateTest2(self, **kw):
        filter = []
        return jqgridDataGrabber(Tracker, 'id', filter, kw).updateGrid()





    @expose('myproject.templates.makoconnection.phonebook')
    def phonebook(self):
        return dict()

    @expose('json')
    def loadPhoneBook(self, **kw):
        filter = []
        return jqgridDataGrabber(PhoneBook, 'id', filter, kw).loadGrid()

    @expose('json')
    def updatePhoneBook(self, **kw):
        filter = []
        return jqgridDataGrabber(PhoneBook, 'id', filter, kw).updateGrid()

    @expose('json')
    def loanTemplate(self, **kw):
        list = []
        loantemplate = render_template({"list": list}, "mako", 'myproject.templates.makoconnection.loantemplate')
        return dict(loantemplate=loantemplate)

    @expose('json')
    def addLoan(self, **kw):
        phone_id = kw["phone_id"]
        amount = kw["amount"]
        due_date = kw["due_date"]
        query = DBSession.query(PhoneBook).filter_by(id=phone_id).first()
        if query is not None:
            newLoan = Loans()
            newLoan.phone_id = phone_id
            newLoan.amount = amount
            newLoan.due_date = due_date
            query.loans.append(newLoan)
            DBSession.add(newLoan)
            DBSession.flush()
        return dict(ok="ok")

    @expose('json')
    def displayLoanTemplate(self, **kw):
        displayloantemplate = render_template({"loanid": kw['id']}, "mako", 'myproject.templates.makoconnection.displayloantemplate')
        return dict(displayloantemplate=displayloantemplate)

    @expose('json')
    def loadjqgridloans(self, **kw):
        filter = [('phonebook_id', 'eq', kw['loanid'])]
        return jqgridDataGrabber(Loans, 'id', filter, kw).loadGrid()

'''
   @expose('pythonvenus.templates.inventory.movements.output')
    @require(predicates.not_anonymous())
    def test(self, **kw):
        movements = DBSession.query(MovementType).filter_by(internal_id=kw['internal_id']).all()
        kw['movements'] = []
        for item in movements:
            kw['movements'].append({'id': item.move_type_id, 'movement': item.movement, 'provider': item.provider, 'client': item.client})
        return dict(page='output', kw=kw)


    @expose('json')
    def loadrows(self):
        url = "http://trirand.com/blog/phpjqgrid/examples/jsonp/getjsonp.php?callback=?&qwery=longorders"
        r = requests.get(url)
        json = r.json()
        return dict(total=200, page=1, records=500, rows=json['rows'])

j['weather']=[]
        for item in json['weather']:
            j['weather'].append({'id': item.id, 'main': item.main, 'description': item.description,'icon': item.icon})
        print(j['weather'])
        
tracker = DBSession.query(Tracker).all() #tracker recibe todos los elementos de la base de datos
        kw['tracker'] = [] #Declaramos una nueva lista dentro del diccionario kw que tiene por llave 'tracker'
        for item in tracker: #Iteramos cada elemento que este denro de trecker de la base de datos
            kw['tracker'].append({'id': item.id, 'imei': item.imei, 'ticket': item.ticket, 'name': item.name}) #agregr diccionarios a la lista kw 'tracker'
            
usuario = DBSession.query(Usuario).filter_by(usuario_id=kw['usuario']).all()
        kw['usuario'] = []
        for item in usuario:
            kw['usuario'].append(
                {'usuario_id': item.usuario_id, 'name': item.name, 'age': item.age, 'phone': item.phone, 'email_address': item.email_address, 'created' : item.created})
'''


        

