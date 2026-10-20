# Debug Incorrect Job Ranking

n = int(input())
jobs = [ ]

for _ in range(n):
    title, score = input().rsplit(" ", 1)
    jobs. append( (title, int(score)))

jobs. sort(key = lambda job: job[1], reverse = True)

for rank, (title, score) in enumerate(jobs, start=1):
    print(f"{rank}. {title} - {score}")