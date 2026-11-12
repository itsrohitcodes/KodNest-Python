# Process Job Requirements Using Thread Arguments

import threading

job_title = input().strip()
experience = int(input())
skills = [skill.strip() for skill in input().split(",")]


def process_job_requirements(job_title, experience, skills):
    # Determine the job level.
    if experience == 0:
        role = "Fresher"
    elif experience >= 1 and experience <= 3:
        role = "Junior"
    else:
        role = "Experienced"

    # Count the skills and print the job summary.
    print(f"Job: {job_title} | Level: {role} | Experience: {experience} years | Skills Required: {len(skills)}")


# Create a thread that passes all three values using args.
thread = threading.Thread(
    target=process_job_requirements,
    args=(job_title, experience, skills)
)

# Start the thread.
thread.start()

# Wait for the thread to finish.
thread.join()