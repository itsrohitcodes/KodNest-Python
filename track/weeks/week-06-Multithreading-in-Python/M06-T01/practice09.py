# Load Student and Job Data Using ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor
import time

student_name = input().strip()
student_skills = [skill.strip() for skill in input().split(",")]
job_title = input().strip()
required_skills = [skill.strip() for skill in input().split(",")]


def load_student_data(name, skills):
    time.sleep(0.1)
    # Return the formatted student summary
    return f"Student: {name} | Skills: {len(skills)}"


def load_job_data(title, skills):
    time.sleep(0.1)
    # Return the formatted job summary
    return f"Job: {title} | Requirements: {len(skills)}"


# Create a ThreadPoolExecutor with two workers.
with ThreadPoolExecutor(max_workers=2) as executor:
    # Submit both loading tasks before collecting either result.
    student_future = executor.submit(load_student_data, student_name, student_skills)
    job_future = executor.submit(load_job_data, job_title, required_skills)

    # Print the student's result, then the job's result.
    print(student_future.result())
    print(job_future.result())

# Print "Data loading completed" after both results are available.
print("Data loading completed")