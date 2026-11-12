# Run Student Profile Processing in a Thread

import threading

name = input().strip()
experience = int(input())
skill = input().strip()


def process_profile():
    # Display the student's profile
    print(f"Student profile ready: {name} ({experience} years, {skill})")


# Create a thread for process_profile()
thread = threading.Thread(target=process_profile)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()