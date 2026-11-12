# Process Multiple Job Data Requests Using a Thread Pool

from concurrent.futures import ThreadPoolExecutor
import time

job_data = {
    "J101": ("Python Developer", 3),
    "J102": ("Data Analyst", 0),
    "J103": ("QA Engineer", 2),
    "J104": ("Frontend Developer", 5),
    "J105": ("DevOps Engineer", 1)
}

n = int(input())
job_ids = [input().strip() for _ in range(n)]


def load_job_data(job_id):
    time.sleep(0.05)

    title, vacancies = job_data[job_id]
    status = "Open" if vacancies > 0 else "Closed"

    summary = f"{job_id}: {title} | Vacancies: {vacancies} | Status: {status}"

    is_open = vacancies > 0

    return summary, is_open


with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [
        executor.submit(load_job_data, job_id)
        for job_id in job_ids
    ]

    results = [future.result() for future in futures]


open_count = 0

for summary, is_open in results:
    print(summary)

    if is_open:
        open_count += 1

print(f"Open Jobs: {open_count}")