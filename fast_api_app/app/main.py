from fastapi import FastAPI, HTTPException
from fast_api_app.app.models.schema import StudentResults, EligibilityResponse
from fast_api_app.app.crud.eligibility_check import check_eligibility

app = FastAPI()

@app.post("/check-eligibility", response_model=EligibilityResponse)
def check_student_eligibility(results: StudentResults):
    try:
        eligibility = check_eligibility(results)
        return eligibility
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
