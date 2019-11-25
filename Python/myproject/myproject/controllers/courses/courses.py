# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose
from myproject.model import DBSession
import transaction
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
        print(kw)
        filter = []
        return jqgridDataGrabber(Student, 'student_id', filter, kw).updateGrid()

    @expose('json')
    def loadProfessor(self, **kw):
        filter = []
        return jqgridDataGrabber(Professor, 'professor_id', filter, kw).loadGrid()

    @expose('json')
    def updateProfessor(self, **kw):
        print(kw)
        filter = []
        return jqgridDataGrabber(Professor, 'professor_id', filter, kw).updateGrid()

    @expose('json')
    def loadRegistered(self, **kw):
        registros = DBSession.query(student_course_table).all()
        relacion = []
        for registro in registros:
            student = DBSession.query(Student).filter_by(student_id=registro.student_id).first()
            course = DBSession.query(Course).filter_by(course_id=registro.course_id).first()
            relacion.append({'student_id': student.student_id, 'course_id': course.course_id, 'student_name': student.name, 'course_name': course.name })
        return dict(total=200, page=1, records=500, rows=relacion)

    @expose('json')
    def updateRegistered(self, **kw):
        print(kw)
        current_student = DBSession.query(Student).filter_by(student_id=kw["student_id"]).first()
        current_course = DBSession.query(Course).filter_by(code=kw["course_name"]).first()
        current_student.courses.append(current_course)
        DBSession.flush()
        return dict(total=200, page=1, records=500, rows=kw)

    @expose('json')
    def DeleteRegistered(self, **kw):
        print(kw)
        student_id = kw["student_id"]
        course_id = kw["course_id"]
        print(student_id)
        print(course_id)
        current_student = DBSession.query(Student).filter_by(student_id=student_id).first()
        current_course = DBSession.query(Course).filter_by(course_id=course_id).first()
        current_student.courses.remove(current_course)
        DBSession.flush()
        return dict()

    @expose('json')
    def loadSubGridCursos(self, **kw):
        relacion = []
        print(kw)
        current_student = DBSession.query(Student).filter_by(student_id=kw["student_id"]).first()#
        for item in current_student.courses:
            print(item.course_id)
            relacion.append({'course_id': item.course_id, 'code': item.code, 'name': item.name })
        print(relacion)
        return dict(total=200, page=1, records=500, rows=relacion)

