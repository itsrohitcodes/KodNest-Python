# Rank Participants Using Score and Completion Time

n = int(input())
participants = []

for _ in range(n):
    name, score, completion_time = input().split()

    participants.append(
        (name, int(score), int(completion_time))
    )

# Write your code here
sorted_participants = sorted(participants, key = lambda i : (-i[1], i[2], i[0]))

for name, score, time in sorted_participants:
    print(name, score, time)