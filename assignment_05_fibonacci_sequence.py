# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


#PART A
number_input = int(input('How many terms?'))

def fibonacci_sequence(number):
    values = []
    first, next = 0, 1
    for i in range(number):
        values.append(first)
        first, next = next, first + next
    return values 

result = fibonacci_sequence(number_input)
print(f'Fibonacci sequence: {' '.join(str(x) for x in result)}')   

#PART 4
checker_input = int(input('Enter a number to check: '))

def is_fibonacci(number):
    first, next = 0, 1
    while first < number:
        first, next = next, first + next
    return first == number


final_result = is_fibonacci(checker_input)

if final_result == True:
    print (f'{checker_input} is a Fibonacci number.')
else: 
    print(f'{checker_input} is NOT a Fibonacci number.')