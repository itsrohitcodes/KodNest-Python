# Add Logging Using a Decorator

def log_operation(function):
    # Write your code here
    def wrapper(name):
        print("Operation started")
        function(name)
        print("Operation completed")
    return wrapper

@log_operation
def display_student (name):
    print("Student:", name)

name = input()
display_student (name)