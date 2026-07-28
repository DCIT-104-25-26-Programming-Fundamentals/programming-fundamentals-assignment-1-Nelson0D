# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def matrix_input (rows, columns):
    matrix = []
    for i in range(rows):
            row = list(map(int, input(f'Enter row {i + 1}: ').split()))
            matrix.append(row)
    return matrix

def matrix_print (matrix):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()


def matrix_transpose(matrix, rows, columns):
    result = []
    for i in range(columns):
        new_row = []
        for n in range(rows):
            new_row.append(matrix[n][i])
        result.append(new_row)
    return result

def matrix_addition(A, B, rows, columns):
    result = []
    for i in range(rows):
        new_row = []
        for n in range(columns):
            new_row.append(A[i][n] + B[i][n])
        result.append(new_row)
    return result


def matrix_multiplicaton(A, B, m, n, p):
    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for x in range(n):
                total += A[i][x] + B[x][j]
            new_row.append(total)
        result.append(new_row)
    return result

#PART A
rows = int(input('Enter number of rows: '))
columns = int(input('Enter number of columns: '))
matrix = matrix_input(rows, columns)
print('Transpose of Matrix: ')
matrix_print(matrix_transpose(matrix, rows, columns))

#PART B
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
print("Matrix A:")
A = matrix_input(rows, columns)
print("Matrix B:")
B = matrix_input(rows, columns)
print("Sum:")
matrix_print(matrix_addition(A, B, rows, columns))

#PART C
m = int(input("Enter rows of A: "))
n = int(input("Enter columns of A (Should be same as rows of B): "))
p = int(input("Enter columns of B: "))
print("Matrix A:")
A = matrix_input(m, n)
print("Matrix B:")
B = matrix_input(n, p)
print("Product:")
matrix_print(matrix_multiplicaton(A, B, m, n, p))