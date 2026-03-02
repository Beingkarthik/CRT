def student_grade_system(name, grades):
    if len(grades) == 0:
        return "No grades provided"

    average = sum(grades) / len(grades)

    if average >= 40:
        status = "Pass"
    else:
        status = "Fail"

    return f"Average grade: {average:.2f}, Status: {status}"