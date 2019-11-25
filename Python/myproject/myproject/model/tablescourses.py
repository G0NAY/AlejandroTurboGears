from sqlalchemy import Table, ForeignKey, Column, Integer, Unicode, DateTime, Numeric, LargeBinary
from myproject.model import DeclarativeBase, metadata
from sqlalchemy.orm import relation, backref, relationship

student_course_table = Table('student_course', metadata,
                         Column('student_id', Integer,
                                ForeignKey('student.student_id',
                                           onupdate="CASCADE",
                                           ondelete="CASCADE"),
                                primary_key=True),
                         Column('course_id', Integer,
                                ForeignKey('course.course_id',
                                           onupdate="CASCADE",
                                           ondelete="CASCADE"),
                                primary_key=True))


class Student(DeclarativeBase):
    __tablename__ = 'student'

    student_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(30))
    lastname = Column(Unicode(30))
    image = Column(LargeBinary(length=(2 ** 32) - 1))

class Course(DeclarativeBase):
    __tablename__ = 'course'

    course_id = Column(Integer, autoincrement=True, primary_key=True)
    code = Column(Unicode(10))
    name = Column(Unicode(30))
    students = relation('Student', secondary=student_course_table, backref='courses')

class Professor(DeclarativeBase):
    __tablename__ = 'professor'

    professor_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(30))
    lastname = Column(Unicode(30))
    courses_name = Column(Unicode(30))
