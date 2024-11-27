from pydantic import BaseModel

class StudentResults(BaseModel):
    student_id: str
    degree_id: str
    credits_earned: int
    gpa: float
    practical_credits: int
    years_taken: int

class EligibilityResponse(BaseModel):
    student_id: str
    degree_id: str
    eligible: bool
    message: str
