tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


# As a user, to manage my task list I would like a program that allows me to:

# 1. Print a list of uncompleted tasks
print("QUESTION 1")

def uncompleted_tasks(list_of_tasks):
    for task in list_of_tasks:
        if task["completed"] == False:
            print(task)

uncompleted_tasks(tasks)

# 2. Print a list of completed tasks
print("QUESTION 2")

def completed_tasks(list_of_tasks):
    for task in list_of_tasks:
        if task["completed"] == True:
            print(task)

completed_tasks(tasks)

# 3. Print a list of all task descriptions
print("QUESTION 3")

def all_tasks(list_of_tasks):
    for task in list_of_tasks:
        print(task["description"])

all_tasks(tasks)

# 4. Print a list of tasks where time_taken is at least a given time
print("QUESTION 4")

def tasks_longer_than_time(list_of_tasks, time):
    for task in list_of_tasks:
        if task["time_taken"] >= time:
            print(task)

tasks_longer_than_time(tasks, 20)

# 5. Print any task with a given description
print("QUESTION 5")

def task_from_description(list_of_tasks, given_description):
    for task in list_of_tasks:
        if task["description"] == given_description:
            print(task)

task_from_description(tasks, "Feed Cat")

# 6. Given a description update that task to mark it as complete.
print("QUESTION 6")

def update_task_progress(list_of_tasks, given_description):
    for task in list_of_tasks:
        if task["description"] == given_description:
            task["completed"] = True

update_task_progress(tasks, "Wash Dishes")
print(tasks[0])

# 7. Add a task to the list
print("QUESTION 7")

def add_task(list_of_tasks, task_description, status, task_length):
    list_of_tasks.append(
        {
            "description": task_description,
            "completed": status,
            "time_taken": task_length
        }
    )

add_task(tasks, "Hoover", False, 25)
print(tasks)

#8. Use a while loop to display the following menu and allow the user to enter an option.
#9. Call the appropriate function depending on the users choice.
print("QUESTIONS 8 & 9")

def task_menu(list_of_tasks):

    user_input = ""

    while user_input == "":
        print("Menu:")
        print("1: Display all tasks")
        print("2: Display uncompleted tasks")
        print("3: Display completed tasks")
        print("4: Mark task as complete")
        print("5: Get tasks which take longer than a given time")
        print("6: Find task by description")
        print("7. Add a new task to list")
        print("M or m: Display this menu")
        print("Q or q: Quit")

        user_input = input("Please select the relevant menu item: ")

        if user_input == "1":
            all_tasks(list_of_tasks)
        elif user_input == "2":
            uncompleted_tasks(list_of_tasks)
        elif user_input == "3":
            completed_tasks(list_of_tasks)
        elif user_input == "4":
            completed_task = input("Please enter the description of the task you would like to mark as completed: ")
            update_task_progress(list_of_tasks, completed_task)
        elif user_input == "5":
            min_time = input("Please enter the minimum length of time for the task: ")
            tasks_longer_than_time(list_of_tasks, int(min_time))
        elif user_input == "6":
            task_description = input("Please enter the description for the task: ")
            task_from_description(list_of_tasks, task_description) 
        elif user_input == "7":
            new_description = input("Please enter a description for the task to be added: ")
            new_status = input("Please enter the status of the task to be added: ")
            new_time = input("Please enter the time required for the task to be added: ")
            add_task(list_of_tasks, new_description, new_status, new_time)
        elif user_input.lower() == "m":
            task_menu(list_of_tasks)
        elif user_input.lower() == "q":
            break
        else:
            user_input = ""

task_menu(tasks)
