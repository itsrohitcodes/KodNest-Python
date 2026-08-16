# Fix a mutable default list bug

# Define the function to add the task
def add_task(task, tasks=None):
    # checking if the list is none
    if tasks is None:
        tasks = []
    # appending the task to the list
    tasks.append(task)
    return tasks

# calling the function
print(add_task("Learn Python")) 
print(add_task("Practice Functions"))