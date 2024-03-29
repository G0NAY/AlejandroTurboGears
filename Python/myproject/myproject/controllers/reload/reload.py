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

__all__ = ['ReloadController']


class ReloadController(BaseController):

    def __init___(self):
        pass

    @expose('myproject.templates.reload.reload')
    def JsonReload(self):
        return dict()

    @expose('json')
    def loadJsonReload(self, **kw):

        rows= [
                {"OrderID": "10248", "OrderDate": "1996-07-04", "CustomerID": "WILMK",
                 "ShipName": "Vins et alcools Chevalier", "Freight": "32.3800"},
                {"OrderID": "10249", "OrderDate": "1996-07-05", "CustomerID": "TRADH",
                 "ShipName": "Toms Spezialit\u00e4ten", "Freight": "11.6100"},
                {"OrderID": "10250", "OrderDate": "1996-07-08", "CustomerID": "HANAR", "ShipName": "Hanari Carnes",
                 "Freight": "65.8300"},
                {"OrderID": "10251", "OrderDate": "1996-07-08", "CustomerID": "VICTE",
                 "ShipName": "Victuailles en stock", "Freight": "41.3400"},
                {"OrderID": "10252", "OrderDate": "1996-07-09", "CustomerID": "SUPRD",
                 "ShipName": "Supr\u00eames d\u00e9lices", "Freight": "51.3000"},
                {"OrderID": "10253", "OrderDate": "1996-07-10", "CustomerID": "HANAR", "ShipName": "Hanari Carnes",
                 "Freight": "58.1700"},
                {"OrderID": "10254", "OrderDate": "1996-07-11", "CustomerID": "CHOPS", "ShipName": "Chop-suey Chinese",
                 "Freight": "22.9800"},
                {"OrderID": "10255", "OrderDate": "1996-07-12", "CustomerID": "RICSU", "ShipName": "Richter Supermarkt",
                 "Freight": "148.3300"},
                {"OrderID": "10256", "OrderDate": "1996-07-15", "CustomerID": "WELLI",
                 "ShipName": "Wellington Importadora", "Freight": "13.9700"},
                {"OrderID": "10257", "OrderDate": "1996-07-16", "CustomerID": "HILAA",
                 "ShipName": "HILARI\u00d3N-Abastos", "Freight": "81.9100"},
                {"OrderID": "10258", "OrderDate": "1996-07-17", "CustomerID": "ERNSH", "ShipName": "Ernst Handel",
                 "Freight": "140.5100"},
                {"OrderID": "10259", "OrderDate": "1996-07-18", "CustomerID": "CENTC",
                 "ShipName": "Centro comercial Moctezuma", "Freight": "3.2500"},
                {"OrderID": "10260", "OrderDate": "1996-07-19", "CustomerID": "OLDWO",
                 "ShipName": "Ottilies K\u00e4seladen", "Freight": "55.0900"},
                {"OrderID": "10261", "OrderDate": "1996-07-19", "CustomerID": "QUEDE", "ShipName": "Que Del\u00edcia",
                 "Freight": "3.0500"},
                {"OrderID": "10262", "OrderDate": "1996-07-22", "CustomerID": "RATTC",
                 "ShipName": "Rattlesnake Canyon Grocery", "Freight": "48.2900"},
                {"OrderID": "10263", "OrderDate": "1996-07-23", "CustomerID": "ERNSH", "ShipName": "Ernst Handel",
                 "Freight": "146.0600"},
                {"OrderID": "10264", "OrderDate": "1996-07-24", "CustomerID": "FOLKO",
                 "ShipName": "Folk och f\u00e4 HB", "Freight": "3.6700"},
                {"OrderID": "10265", "OrderDate": "1996-07-25", "CustomerID": "BLONP",
                 "ShipName": "Blondel p\u00e8re et fils", "Freight": "55.2800"},
                {"OrderID": "10266", "OrderDate": "1996-07-26", "CustomerID": "WARTH", "ShipName": "Wartian Herkku",
                 "Freight": "25.7300"},
                {"OrderID": "10267", "OrderDate": "1996-07-29", "CustomerID": "FRANK", "ShipName": "Frankenversand",
                 "Freight": "208.5800"},
                {"OrderID": "10268", "OrderDate": "1996-07-30", "CustomerID": "GROSR",
                 "ShipName": "GROSELLA-Restaurante", "Freight": "66.2900"},
                {"OrderID": "10269", "OrderDate": "1996-07-31", "CustomerID": "WHITC",
                 "ShipName": "White Clover Markets", "Freight": "4.5600"},
                {"OrderID": "10270", "OrderDate": "1996-08-01", "CustomerID": "WARTH", "ShipName": "Wartian Herkku",
                 "Freight": "136.5400"},
                {"OrderID": "10271", "OrderDate": "1996-08-01", "CustomerID": "SPLIR",
                 "ShipName": "Split Rail Beer & Ale", "Freight": "4.5400"},
                {"OrderID": "10272", "OrderDate": "1996-08-02", "CustomerID": "RATTC",
                 "ShipName": "Rattlesnake Canyon Grocery", "Freight": "98.0300"},
                {"OrderID": "10273", "OrderDate": "1996-08-05", "CustomerID": "QUICK", "ShipName": "QUICK-Stop",
                 "Freight": "76.0700"},
                {"OrderID": "10274", "OrderDate": "1996-08-06", "CustomerID": "VINET",
                 "ShipName": "Vins et alcools Chevalier", "Freight": "6.0100"},
                {"OrderID": "10275", "OrderDate": "1996-08-07", "CustomerID": "MAGAA",
                 "ShipName": "Magazzini Alimentari Riuniti", "Freight": "26.9300"},
                {"OrderID": "10276", "OrderDate": "1996-08-08", "CustomerID": "TORTU",
                 "ShipName": "Tortuga Restaurante", "Freight": "13.8400"},
                {"OrderID": "10277", "OrderDate": "1996-08-09", "CustomerID": "MORGK",
                 "ShipName": "Morgenstern Gesundkost", "Freight": "125.7700"}
        ]

        return dict(total=200, page=1, records=500, rows=rows)
