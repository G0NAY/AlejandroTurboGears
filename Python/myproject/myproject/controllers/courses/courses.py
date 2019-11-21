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
from myproject.model.tablescourses import Course, Student, Professor, student_course_table
from myproject.controllers.jqgrid import jqgridDataGrabber

from myproject.lib.base import BaseController

__all__ = ['CoursesController']


class CoursesController(BaseController):

    def __init___(self):
        pass

    @expose('myproject.templates.courses.courses')
    def CoursesLoad(self):
        return dict()

    @expose('json')
    def loadCourses(self, **kw):
        filter = []
        return jqgridDataGrabber(Course, 'course_id', filter, kw).loadGrid()

    @expose('json')
    def updateCourses(self, **kw):
        filter = []
        return jqgridDataGrabber(Course, 'course_id', filter, kw).updateGrid()

    @expose('json')
    def loadStudent(self, **kw):
        filter = []
        return jqgridDataGrabber(Student, 'student_id', filter, kw).loadGrid()

    @expose('json')
    def updateStudent(self, **kw):
        filter = []
        return jqgridDataGrabber(Student, 'student_id', filter, kw).updateGrid()

    @expose('json')
    def loadProfessor(self, **kw):
        filter = []
        return jqgridDataGrabber(Professor, 'professor_id', filter, kw).loadGrid()

    @expose('json')
    def updateProfessor(self, **kw):
        filter = []
        return jqgridDataGrabber(Professor, 'professor_id', filter, kw).updateGrid()