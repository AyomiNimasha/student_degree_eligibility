from fastapi import FastAPI, HTTPException
from models import StudentResults, EligibilityResponse
from eligibility_check import check_eligibility

app = FastAPI()

@app.post("/check-eligibility", response_model=EligibilityResponse)
def check_student_eligibility(results: StudentResults):
    try:
        eligibility = check_eligibility(results)
        return eligibility
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
