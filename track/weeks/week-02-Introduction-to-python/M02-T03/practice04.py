# Update a Tuple without modifying it

# Read the course details
course_name = input()
course_week = input()
course_status = input()

# Create the original tuple
course_details = (course_name, course_week, course_status)

# Read the updated week
course_week = input()

# Create and assign a new tuple
course_details = (course_name, course_week, course_status)

# Display the updated tuple
print(course_details)