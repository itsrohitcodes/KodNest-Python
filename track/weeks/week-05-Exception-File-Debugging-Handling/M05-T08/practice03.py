# Display Messages Before and After Execution

def result_notification(function):
    # Write your code here
    def wrapper(name, score):
        print("Result processing started")
        result = function(name, score)
        print("Result processing finished")
        return result
    return wrapper

@result_notification
def show_result(name, score):
    print(f"{name} scored {score}")

name = input()
score = int(input())
show_result(name, score)