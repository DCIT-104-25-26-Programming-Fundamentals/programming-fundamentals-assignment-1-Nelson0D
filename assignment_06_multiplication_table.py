# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

#Part A

input_1 = int(input('Enter a number for the multiplication table: '))
if input_1 <= 0:
    print('Error: Number must be a positive integer')
    exit()
multiplication_ans = []

def multiplication_gen(input_1):
    print(f'Multiplication table for {input_1}: ')
    for i in range(1, 13):
        new_value = input_1 * i
        print(f'{input_1} x {i} = {new_value} ')
    return ''
result = multiplication_gen(input_1)
print(result)


#Part B
input_2 = int(input('Enter a number for the multiplication table: '))
if input_2 <= 0:
    print('Error: Number must be a positive integer: ')
    exit()

for n in range(1, input_2):
    value = multiplication_gen(n)
    print(value)
    print('---------------')

