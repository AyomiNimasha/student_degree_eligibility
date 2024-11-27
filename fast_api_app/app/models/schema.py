from pydantic import BaseModel
from datetime import date
import enum,email

class Student(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    email: email
    enrolled_date : date
    acaademic_year : str
    user_name : str
    password : str

class Degree(BaseModel):
    degree_combination_id : str
    degree_id : str
    combination_id : int
    degree_name : str
    gpa_min : float
    max_years : int


class Degree_enrollment(BaseModel):
    degree_enrollment_id: int
    Degree_enrollment_date: date
    student_id: str 
    degree_combination_id: str
    academic_year: str
    Degree_enrollment_status: enum

    
class Courses(BaseModel):
    course_id : str
    course_code : str
    course_name : str
    course_type : enum
    course_status : enum
    department_id : str
    academic_level : int
    semester : int
    credits : int
    gpa_count : bool

class Course_relationship(BaseModel):
    course_id : str
    related_course_id : str 
    relationship_type : enum 

class Department(BaseModel):
    department_id : int 
    department_name : str
    faculty : enum

class Course_enrollment(BaseModel):
    enrollment_id : int
    enrollment_date : date
    student_id : str 
    degree_combination_id : str 
    course_id : str 
    academic_year : str 
    semester : int 
    enrollment_status : enum

class Exam(BaseModel):
    exam_id : str
    academic_year : str
    academic_level : int
    semester : int 
    exam_date : date
    exam_type : enum 

class Course_marks(BaseModel):
    Student_id : str
    exam_id : str
    course_id : str 
    attempt_number : int 
    marks : int 
    grade : str
    result_date : date

class Grades(BaseModel):
    grade : str
    mark_range : str 
    gp : float 
    