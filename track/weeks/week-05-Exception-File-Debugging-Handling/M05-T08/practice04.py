# Create a Simple Function Execution Tracker

def track_execution(function):
    # Write your code here
    count = 0
    def wrapper (score):
        nonlocal count
        count += 1

        print(f"Execution count: {count}")
        result = function(score)
        return result

    return wrapper

@track_execution
def check_score(score):
    if score >= 60:
        return "Pass"
    return "Fail"

n = int(input())

if n == 0:
    print("No checks performed")
else:
    for _ in range(n):
        score = int(input())
        print (check_score(score))