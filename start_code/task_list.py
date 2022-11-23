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

def uncompleted_tasks():
    for task in tasks:
        if task["completed"] == False:
            print(task)

uncompleted_tasks()

# 2. Print a list of completed tasks
print("QUESTION 2")

def completed_tasks():
    for task in tasks:
        if task["completed"] == True:
            print(task)

completed_tasks()

# 3. Print a list of all task descriptions
print("QUESTION 3")

def all_tasks():
    for task in tasks:
        print(task["description"])

all_tasks()

# 4. Print a list of tasks where time_taken is at least a given time
print("QUESTION 4")

def tasks_longer_than_time(time):
    for task in tasks:
        if task["time_taken"] >= time:
            print(task)

tasks_longer_than_time(20)

# 5. Print any task with a given description
print("QUESTION 5")

def task_from_description(given_description):
    for task in tasks:
        if task["description"] == given_description:
            print(task)

task_from_description("Feed Cat")

# 6. Given a description update that task to mark it as complete.
print("QUESTION 6")

def update_task_progress(given_description):
    for task in tasks:
        if task["description"] == given_description:
            task["completed"] = True

update_task_progress("Wash Dishes")
print(tasks[0])

# 7. Add a task to the list
print("QUESTION 7")

def add_task(task_description, status, task_length):
    tasks.append(
        {
            "description": task_description,
            "completed": status,
            "time_taken": task_length
        }
    )

add_task("Hoover", False, 25)
print(tasks)

#8. Use a while loop to display the following menu and allow the user to enter an option.
#9. Call the appropriate function depending on the users choice.
# print("QUESTIONS 8 & 9")

# def task_menu():

#     user_input = "m"

#     while user_input.lower() == "m":
#         print("Menu:")
#         print("1: Display all tasks")
#         print("2: Display uncompleted tasks")
#         print("3: Display completed tasks")
#         print("4: Mark task as complete")
#         print("5: Get tasks which take longer than a given time")
#         print("6: Find task by description")
#         print("7. Add a new task to list")
#         print("M or m: Display this menu")
#         print("Q or q: Quite")

#         user_input = input("Please select the relevant menu item: ")
#         if user_input == "1":
#             #list of all tasks
#         elif user_input == "2":
#             uncompleted_tasks()
#         elif user_input == "3":
#             completed_tasks()
#         elif user_input == "4":
#             update_task_progress() #NEED TO ADD WAY OF ENTERING TASK DESCRIPTION
#         elif user_input == "5":
#             tasks_longer_than_time() #NEED TO ADD WAY OF ENTERING TIME
#         elif user_input == "6":
#             task_from_description()  #NEED TO ADD WAY OF ENTERING TASK DESCRIPTION
#         elif user_input == "7":
#             add_task()  #NEED TO ADD WAY OF ENTERING TASK INFO

# task_menu()
