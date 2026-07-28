# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

commands = ['Add student', 'Display all students', 'Calculate average score', "Quit"]

choice = None

students = []


def add_student():
    student_name = str(input('Student Name: '))
    student_id = int(input('Student ID: '))
    num_scores = int(input('How many scores? '))
    scores = []

    for i in range(1, num_scores + 1):
          score_values = int(input(f'Enter number {i}: '))
          scores.append(score_values)
    student = {
          'name': student_name.capitalize(),
        'id': student_id,
        'scores': scores
    }
    students.append(student)
    print(f'Student "{student_name}" added succesfully.')
    return '--------------------------------------------'

def view_all_students():
    if not students:
          print('No student has been added yet!')
          return '------------------------'
    print('-' * 70)
    print(f'{"Names": <15} {"ID": <15} {"Scores": <15} {"Average": <15}')
    
    for i in students:
           sum_val = 0
           for n in i['scores']:
                sum_val += n
           average = round(sum_val / len(i['scores']), 2)
           str_scores = ', '.join(str(s) for s in i['scores'])
           print('-'*70)
           print(f'{i["name"]: <15}  {i["id"]: <15}{str_scores: <15} {average: <15}')
    return '-' * 70

def calculate_average():
    student_id = int(input('Enter student ID: '))
    for i in students:
         if i['id'] == student_id:
            sum_val = 0
            for n in i['scores']:
                 sum_val += n
            average = round(sum_val / len(i['scores']), 2)
            return(f"{i["name"]}'s average score: {average}")
    return ('Error, ID does not exist')

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
        result = add_student()
        print(result)
    elif choice_input == 2:
         result = view_all_students()
         print(result)
    elif choice_input == 3:
        result = calculate_average()
        print(result)
    elif choice_input == 4:
         result = quit()
    else:
         print('Error: Invalid command input (1-4). Try again \n ------------------------')
         