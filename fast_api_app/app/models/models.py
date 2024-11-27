from sqlalchemy import Column, String, Integer, Float, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum


# Enums
class CourseTypeEnum(str, enum.Enum):
    compulsory = "Compulsory"
    optional = "Optional"
    auxiliary = "Auxiliary"

class StatusEnum(str, enum.Enum):
    active = "Active"
    inactive = "Inactive"
    completed = "Completed"

class CourseRelationEnum(str, enum.Enum):
    prerequisite = "Prerequisite"
    corequisite = "Corequisite"

class ExamEnum(str, enum.Enum):
    final = "Final"
    mid = "Mid"

# Models
class Student(Base):
    __tablename__ = "students"
    student_id = Column(String, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    enrolled_date = Column(Date, nullable=False)
    academic_year = Column(String, nullable=False)
    user_name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    degree_enrollments = relationship("DegreeEnrollment", back_populates="student")
    course_enrollments = relationship("CourseEnrollment", back_populates="student")
    course_marks = relationship("CourseMarks", back_populates="student")

class Degree(Base):
    __tablename__ = "degrees"
    degree_combination_id = Column(String, primary_key=True)
    degree_id = Column(String, nullable=False)
    combination_id = Column(Integer, nullable=False)
    degree_name = Column(String, nullable=False)
    gpa_min = Column(Float, nullable=False)
    max_years = Column(Integer, nullable=False)

    degree_enrollments = relationship("DegreeEnrollment", back_populates="degree")

class DegreeEnrollment(Base):
    __tablename__ = "degree_enrollments"
    degree_enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    degree_enrollment_date = Column(Date, nullable=False)
    student_id = Column(String, ForeignKey("students.student_id"), nullable=False)
    degree_combination_id = Column(String, ForeignKey("degrees.degree_combination_id"), nullable=False)
    academic_year = Column(String, nullable=False)
    degree_enrollment_status = Column(Enum(StatusEnum), nullable=False)

    student = relationship("Student", back_populates="degree_enrollments")
    degree = relationship("Degree", back_populates="degree_enrollments")

class Course(Base):
    __tablename__ = "courses"
    course_id = Column(String, primary_key=True)
    course_code = Column(String, nullable=False)
    course_name = Column(String, nullable=False)
    course_type = Column(Enum(CourseTypeEnum), nullable=False)
    course_status = Column(Enum(StatusEnum), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.department_id"), nullable=False)
    academic_level = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)
    credits = Column(Integer, nullable=False)
    gpa_count = Column(Integer, nullable=False)

    course_enrollments = relationship("CourseEnrollment", back_populates="course")
    course_relationships = relationship("CourseRelationship", back_populates="course")

class CourseEnrollment(Base):
    __tablename__ = "course_enrollments"
    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    enrollment_date = Column(Date, nullable=False)
    student_id = Column(String, ForeignKey("students.student_id"), nullable=False)
    degree_combination_id = Column(String, ForeignKey("degrees.degree_combination_id"), nullable=False)
    course_id = Column(String, ForeignKey("courses.course_id"), nullable=False)
    academic_year = Column(String, nullable=False)
    semester = Column(Integer, nullable=False)
    enrollment_status = Column(Enum(StatusEnum), nullable=False)

    student = relationship("Student", back_populates="course_enrollments")
    course = relationship("Course", back_populates="course_enrollments")

class CourseRelationship(Base):
    __tablename__ = "course_relationships"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(String, ForeignKey("courses.course_id"), nullable=False)
    related_course_id = Column(String, nullable=False)
    relationship_type = Column(Enum(CourseRelationEnum), nullable=False)

    course = relationship("Course", back_populates="course_relationships")

class Department(Base):
    __tablename__ = "departments"
    department_id = Column(Integer, primary_key=True, nullable=False)
    department_name = Column(String, nullable=False)
    faculty = Column(String, nullable=False)

    courses = relationship("Course", back_populates="department")

class Exam(Base):
    __tablename__ = "exams"
    exam_id = Column(String, primary_key=True, nullable=False)
    academic_year = Column(String, nullable=False)
    academic_level = Column(String, nullable=False)
    semester = Column(Integer, nullable=False)
    exam_date = Column(Date, nullable=False)
    exam_type = Column(Enum(ExamEnum), nullable=False)

    course_marks = relationship("CourseMarks", back_populates="exam")

class CourseMarks(Base):
    __tablename__ = "course_marks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(String, ForeignKey("students.student_id"), nullable=False)
    exam_id = Column(String, ForeignKey("exams.exam_id"), nullable=False)
    course_id = Column(String, ForeignKey("courses.course_id"), nullable=False)
    attempt_number = Column(Integer, nullable=False)
    marks = Column(Integer, nullable=False)
    grade = Column(String, nullable=False)
    result_date = Column(Date, nullable=False)

    student = relationship("Student", back_populates="course_marks")
    exam = relationship("Exam", back_populates="course_marks")
    grades = relationship("Course_marks",back_populates="Course_marks")


class Grade(Base):
    __tablename__ = "grades"
    grade = Column(String,primary_key=True,nullable=False)
    mark_range = Column(String,nullable=False)
    gp = Column(float,nullable=False)

    Course_marks = relationship("Course_marks",back_populates="grade")
