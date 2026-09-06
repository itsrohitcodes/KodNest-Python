# Build a Training Batch Class Using Instance, Class and Static Method

class TrainingBatch:
    batch_name = "Python Batch 1"
    student_count = 0

    def __init__(self, student_name, attendance):
        # Store the student data
        self.student_name = student_name
        self.attendance = attendance
        # Increase the shared student count
        TrainingBatch.student_count += 1

    def get_details(self):
        # Return the formatted student details
        return f"{self.student_name}: {self.attendance}%"

    # Create the update_batch_name() class method
    @classmethod
    def update_batch_name(cls, new_batch_name):
        cls.batch_name = new_batch_name

    # Create the is_valid_attendance() static method
    @staticmethod
    def is_valid_attendance(attendance):
        if 0 <= attendance <= 100:
            return True
        else:
            return False


n = int(input())
students = []

# Read n records
# Validate attendance and create valid objects
for _ in range(n):
    student_name = input()
    attendance = int(input())

    if TrainingBatch.is_valid_attendance(attendance):
        student = TrainingBatch(student_name, attendance)
        students.append(student)

new_batch_name = input().strip()

# Update the shared batch name
TrainingBatch.update_batch_name(new_batch_name)

# Print the batch, count and valid student details
print(f"Batch: {TrainingBatch.batch_name}")
print(f"Valid Students: {TrainingBatch.student_count}")

for student in students:
    print(student.get_details())