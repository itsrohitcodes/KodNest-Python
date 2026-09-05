# Manage Shared and Object specific Training Batch Data

class TrainingBatch:
    # Create the shared class variables
    platform_name = "KodNest"
    batch_name = "Python Batch 1"

    def __init__(self, student_name, score):
        # Store the object-specific values
        self.student_name = student_name
        self.score = score


student1_name = input().strip()
student1_score = int(input())

student2_name = input().strip()
student2_score = int(input())

# Create two TrainingBatch objects
s1 = TrainingBatch(student1_name, student1_score)
s2 = TrainingBatch(student2_name, student2_score)

# Print the shared batch information
print(f"Platform: {TrainingBatch.platform_name}")
print(f"Batch: {TrainingBatch.batch_name}")

# Print the information of both students
print(f"Student 1: {s1.student_name}, Score: {s1.score}")
print(f"Student 2: {s2.student_name}, Score: {s2.score}")