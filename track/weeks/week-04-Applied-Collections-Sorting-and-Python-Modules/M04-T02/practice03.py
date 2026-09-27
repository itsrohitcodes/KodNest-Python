# Select Students who scored above the Cutoff

def select_students(students, cutoff):
    # Write your list comprehension here
    pass_students = [student for student in students if student[1] > cutoff]

    return pass_students


students = [
    ["Asha", 78],
    ["Ravi", 55],
    ["Meera", 92],
    ["Kiran", 63],
    ["John", 40]
]

cutoff = int(input())
selected_students = select_students(students, cutoff)

if not selected_students:
    print("No students")
else:
    for student in selected_students:
        print(student[0])