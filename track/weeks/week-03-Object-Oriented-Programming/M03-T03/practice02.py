# Build a Course and CodingCourse Classes

class Course:
    # Add the constructor and display_course()
    def display_course(self, course_name):
        print(f"Course: {course_name}")


class CodingCourse(Course):
    pass


course_name = input().strip()

# Create a CodingCourse object and display the course
course = CodingCourse()

course.display_course(course_name)