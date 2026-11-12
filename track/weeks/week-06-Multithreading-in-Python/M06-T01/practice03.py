# Run Job Requirement Processing in a Thread

import threading

job_title = input().strip()
min_experience = int(input())
max_experience = int(input())


def process_job_requirement():
    # Check the experience range and print the result
    if min_experience > max_experience:
        print(f"Invalid experience range for {job_title}")
    else:
        print(f"Job Requirement Verified: {job_title} ({min_experience} to {max_experience} years)")


# Create a thread to run process_job_requirement()
thread = threading.Thread(target=process_job_requirement)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()