# Generate Student IDs

def generate_student_ids(start, count):
    # Write your code here
    for i in range(count):
        yield start + i

start = int(input())
count = int(input())

student_ids = list(generate_student_ids(start, count))

if student_ids:
    print(*student_ids)
else:
    print("No student IDs")