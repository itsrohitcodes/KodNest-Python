# Run Job Skill Processing in a Thread

import threading

job_title = input().strip()
skills = [skill.strip() for skill in input().split(",")]


def process_job_skills():
    # Remove repeated skills while preserving their order
    unique_skills = []

    for skill in skills:
        if skill not in unique_skills:
            unique_skills.append(skill)

    # Print the job title, unique skills, and unique skill count
    print(f"Job: {job_title} | Skills: {', '.join(unique_skills)} | Unique skill count: {len(unique_skills)}")


# Create a thread to run process_job_skills()
thread = threading.Thread(target=process_job_skills)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()