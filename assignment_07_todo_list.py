# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
commands = ['Add tasks', 'View tasks', 'Delete Task', "Quit"]

choice = None

tasks = []



def add_task():
    description = str(input('Enter task: '))
    tasks.append(description)
    print (f'Task added: "{description}"')
    return '------------------------'

def view_tasks():
     if not tasks:
          print('No tasks yet!')
          return '------------------------'
     print('Your Tasks: ')
     for i in tasks:
          print(f'{tasks.index(i) + 1}. {i}')
     return '------------------------'

def delete_task():
    if not tasks:
              print('No tasks yet!')
              return '------------------------'
    for i in tasks:
               print(f'{tasks.index(i) + 1}. {i}')
    indexOf = int(input('Enter task number to remove: '))
    for x in tasks:
         if indexOf == tasks.index(x) + 1:
            tasks.pop(indexOf-1)
            return f'Task "{x}" has been removed'
    print ('Error: Task does not exist.')
    return '------------------------'

def quit():
     print('Exiting application. Goodbye...')
     print('------------------------')
     exit()




while True:
    for i in commands:
        print(f'{commands.index(i) + 1} {i}')
    print ('------------------------')
    choice_input = int(input('Enter a choice (1-4): '))


    if choice_input == 1:
        result = add_task()
        print(result)
    elif choice_input == 2:
         result = view_tasks()
         print(result)
    elif choice_input == 3:
        result = delete_task()
        print(result)
    elif choice_input == 4:
         result = quit()
    else:
         print('Error: Invalid command input (1-4). Try again \n ------------------------')
         