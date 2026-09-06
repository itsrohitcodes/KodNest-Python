# Manage Shared Platform and Object specific Course data

class Course:
    # Create the shared platform variable
    platform_name = "KodNest Learning"

    def __init__(
        self,
        course_name,
        duration_days,
        fee
    ):
        # Store the object-specific course data
        self.course_name = course_name
        self.duration_days = duration_days
        self.fee = fee


course1_name = input().strip()
course1_duration = int(input())
course1_fee = int(input())

course2_name = input().strip()
course2_duration = int(input())
course2_fee = int(input())

# Create two Course objects
course1 = Course(course1_name, course1_duration, course1_fee)
course2 = Course(course2_name, course2_duration, course2_fee)

# Print the shared platform
print(f"Platform: {Course.platform_name}")

# Print both course records
print(f"Course 1: {course1.course_name}")
print(f"Duration: {course1.duration_days} days")
print(f"Fee: {course1.fee}")

print(f"Course 2: {course2.course_name}")
print(f"Duration: {course2.duration_days} days")
print(f"Fee: {course2.fee}")