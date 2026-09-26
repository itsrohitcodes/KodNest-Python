# Check Course Availability using a Course Code

def check_course_availability(courses, course_code):
    # Write your dictionary lookup logic here
    if course_code not in courses:
        return "Course not found"

    seats = courses.get(course_code)

    if seats == 0:
        return "Course full"
    else:
        return f"Seats available: {seats}"


courses = {
    "PY101": 25,
    "SQL201": 0,
    "DSA301": 12,
    "WEB401": 4
}

course_code = input()
print(check_course_availability(courses, course_code))