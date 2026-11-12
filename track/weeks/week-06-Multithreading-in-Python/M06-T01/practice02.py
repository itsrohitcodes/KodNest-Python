# Run Student Skill Processing in a Thread

import threading

name = input().strip()
skills = [skill.strip() for skill in input().split(",")]


def process_skills():
    # Sort the skills and print the summary
    skills.sort()
    print(f"{name}: {', '.join(skills)} (Total: {len(skills)})")


# Create a thread with process_skills as its target
thread = threading.Thread(target=process_skills)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()