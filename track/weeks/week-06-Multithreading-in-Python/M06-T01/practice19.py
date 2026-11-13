# Control Concurrent Preparation Data Loading

import threading
import time

preparation_data = {
    "P101": ("Python Fundamentals", 12),
    "P102": ("SQL Practice", 8),
    "P103": ("DSA Revision", 15),
    "P104": ("Aptitude", 6),
    "P105": ("Mock Interview", 4),
    "P106": ("Project Review", 10)
}

n = int(input())
selected_plans = []

for _ in range(n):
    plan_id = input().strip()
    completed = int(input())
    selected_plans.append((plan_id, completed))


semaphore = threading.Semaphore(2)
results = [None] * n


def load_plan(index, plan_id, completed):
    # Use with semaphore: for the simulated service request.
    with semaphore:

        # Inside it, wait using time.sleep(0.02) and look up the plan.
        time.sleep(0.02)

        plan_name, required_hours = preparation_data[plan_id]

        # Calculate remaining hours and determine the plan status.
        remaining = required_hours - completed

        if completed == 0:
            status = "Not Started"
        elif remaining == 0:
            status = "Completed"
        else:
            status = "In Progress"

        is_completed = (status == "Completed")

        # Store (message, remaining_hours, is_completed) in results[index].
        message = (
            f"{plan_id} | {plan_name} | Remaining: {remaining} "
            f"hours | Status: {status}"
        )

        results[index] = (message, remaining, is_completed)


threads = []

# Start one worker thread for each selected plan.
for index, (plan_id, completed) in enumerate(selected_plans):
    t = threading.Thread(
        target=load_plan,
        args=(index, plan_id, completed)
    )

    threads.append(t)


for t in threads:
    t.start()


# Wait for every worker to finish.
for t in threads:
    t.join()


# Print the results in input order.
completed_count = 0
total_remaining = 0

for message, remaining, is_completed in results:
    print(message)

    total_remaining += remaining

    if is_completed:
        completed_count += 1


# Print the completed-plan count and remaining hours.
print("Completed Plans:", completed_count)
print("Total Remaining Hours:", total_remaining)