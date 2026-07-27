# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

input_number = int(input('How many numbers? '))
if input_number <= 0:
    print('Error: Input must be a positive integer')
    exit()
numbers = []

for i in range(1, input_number + 1):
    indie_numbers = int(input(f'Enter number {i}: '))
    numbers.append(indie_numbers)


def compute_sum (numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def compute_average(numbers):
    return compute_sum(numbers) / len(numbers)

def compute_max(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest
def compute_min(numbers):
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest


total = compute_sum(numbers)
average = compute_average(numbers)
largest = compute_max(numbers)
smallest = compute_min(numbers)

print('Results: ')
print(f'Sum:     {total}')
print(f'Average: {average}')
print(f'Maximum: {largest}')
print(f'Minimum: {smallest}')