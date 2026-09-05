# Update a Shared Batch Name Using a Class Method

class TrainingBatch:
    batch_name = "Python Batch 1"

    def __init__(self, student_name):
        # Store the student name
        self.student_name = student_name

    # Create the update_batch_name() class method
    @classmethod
    def update_batch_name(cls, new_batch_name):
        cls.batch_name = new_batch_name


student1_name = input().strip()
student2_name = input().strip()
new_batch_name = input().strip()

# Create two TrainingBatch objects
student1 = TrainingBatch(student1_name)
student2 = TrainingBatch(student2_name)

# Update the shared batch name using the class method
TrainingBatch.update_batch_name(new_batch_name)

# Print the updated value through the class and both objects
print(f"Updated Batch: {TrainingBatch.batch_name}")
print(f"{student1.student_name}: {student1.batch_name}")
print(f"{student2.student_name}: {student2.batch_name}")