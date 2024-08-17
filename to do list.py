# Define an empty list to store tasks
todo_list = []

# Function to display the tasks
def display_tasks():
    print("Tasks:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")

# Function to add a task
def add_task(task):
    todo_list.append(task)
    print(f"'{task}' added to the To-Do List.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        new_task = input("Enter a new task: ")
        add_task(new_task)
    elif choice == '3':
        print("Exiting the To-Do List application.")
        break
    else:
        print("Invalid option. Please choose again.")

print("Thank you for using the To-Do List app!")