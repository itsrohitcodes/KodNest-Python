# Collect Preparation Results from Thread Pool Tasks

from concurrent.futures import ThreadPoolExecutor
import time

student_skills = [skill.strip() for skill in input().split(",")]
n = int(input())
jobs = []

for _ in range(n):
    title = input().strip()
    requirements = [skill.strip() for skill in input().split(",")]
    jobs.append((title, requirements))


def prepare_job(record, student_skills):
    time.sleep(0.05)
    # Find missing skills.
    # Return (job_title, missing_count, preparation_hours).
    title, requirements = record

    missing_count = sum(
        1 for skill in requirements
        if skill not in student_skills
    )

    preparation_hours = missing_count * 2

    return title, missing_count, preparation_hours


# Create a thread pool with 3 workers.
with ThreadPoolExecutor(max_workers=3) as executor:

    # Submit all job checks and save their Future objects.
    futures = [
        executor.submit(prepare_job, job, student_skills)
        for job in jobs
    ]

    # Collect results in the input order.
    results = [future.result() for future in futures]


# Print each job summary and the total preparation hours.
total_hours = 0

for title, missing_count, hours in results:
    print(f"{title} | Missing: {missing_count} | Preparation: {hours} hours")

    total_hours += hours

print(f"Total Preparation Hours: {total_hours}")