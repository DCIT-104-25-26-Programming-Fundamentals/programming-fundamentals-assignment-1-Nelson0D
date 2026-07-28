# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

commands = ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Modulus', 'Exponentiation', 'Quit']

def addition():
    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))
    value = first + second
    print (f'{first} + {second} = {value}')
    return '-' * 25
    

def subtraction():
    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))
    value = first - second
    print (f'{first} - {second} = {value}')
    return '-' * 25

def multiplication():
    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))
    value = first * second
    print (f'{first} * {second} = {value}')
    return '-' * 25

def division():
    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))
    if second == 0:
         return 'Error: Cannot divide by 0.'
    value = round(first / second, 2)
    print (f'{first} / {second} = {value}')
    return '-' * 25

def modulus():
    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))
    value = first % second
    print (f'{first} mod {second} = {value}')
    return '-' * 25

def exponentiation():
    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))
    value = first ** second
    print (f'{first} ** {second} = {value}')
    return '-' * 25

def quit():
     print('Exiting application. Goodbye...')
     print('------------------------')
     exit()


while True:

    for i in commands:
              print(f'{commands.index(i) + 1} {i}')
    print ('------------------------')
    choice_input = int(input('Enter a choice (1-7): '))

    if choice_input == 1:
        result = addition()
        print(result)
    elif choice_input == 2:
         result = subtraction()
         print(result)
    elif choice_input == 3:
        result = multiplication()
        print(result)
    elif choice_input == 4:
            result = division()
            print(result)
    elif choice_input == 5:
            result = modulus()
            print(result)
    elif choice_input == 6:
            result = exponentiation()
            print(result)
    elif choice_input == 7:
         result = quit()
    else:
         print('Error: Invalid command input (1-7). Try again \n ------------------------')
         