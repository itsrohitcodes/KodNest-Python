# Display a Message Before Function Execution

def show_welcome(function):
    # Write your code here
    def wrapper(course) :
        print("Welcome to KodNest!")
        return function(course)
    return wrapper

@show_welcome
def show_course(course):
    print("Course:", course)

course = input()
show_course(course)