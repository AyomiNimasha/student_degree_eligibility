from fast_api_app.app.models.schema import StudentResults, EligibilityResponse

def check_eligibility(results: StudentResults) -> EligibilityResponse:
    degree_criteria = {
        "BSc": {
            "min_gpa": 2.0,
            "max_years": 5,
            "min_credits_2_years": 60,
            "min_credits_3_years": 90,
            "min_practical_credits": 48,
        }
    }

    # Retrieve degree requirements
    degree_id = results.degree_id
    if degree_id not in degree_criteria:
        raise ValueError(f"Degree {degree_id} is not recognized.")

    criteria = degree_criteria[degree_id]

    # Validate against the criteria
    if results.gpa < criteria["min_gpa"]:
        return EligibilityResponse(
            student_id=results.student_id,
            degree_id=results.degree_id,
            eligible=False,
            message="GPA does not meet the minimum requirement."
        )

    if results.years_taken > criteria["max_years"]:
        return EligibilityResponse(
            student_id=results.student_id,
            degree_id=results.degree_id,
            eligible=False,
            message="Exceeded the maximum duration allowed for the degree."
        )

    if results.credits_earned < criteria["min_credits_2_years"]:
        return EligibilityResponse(
            student_id=results.student_id,
            degree_id=results.degree_id,
            eligible=False,
            message="Credits earned in 2 years are insufficient."
        )

    if results.practical_credits < criteria["min_practical_credits"]:
        return EligibilityResponse(
            student_id=results.student_id,
            degree_id=results.degree_id,
            eligible=False,
            message="Practical credits are insufficient."
        )

    # If all conditions are met, return eligible
    return EligibilityResponse(
        student_id=results.student_id,
        degree_id=results.degree_id,
        eligible=True,
        message="The student is eligible for the degree."
    )
