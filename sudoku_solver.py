"""

This python script solves a sudoku puzzle. 

"""


import numpy as np


puzzle = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7] ]



## We can create a function to prompt user to input a sudoku puzzle
'''
def get_puzzle():
    puzzle = input("Enter Sudoku puzzle as a list: ")
    return puzzle
'''

## Sudoku puzzle must be a numpy array
#puzzle = get_puzzle()
puzzle = np.array(puzzle)

## Sudoku game solver using the backtracking algorithm.

def print_board(board):
    "Input: A 9x9 array"
    "Returns a grid like Sudoka board"

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])

            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for r in range(len(board)): # len(bo) is 9
        for c in range(len(board[0])): # range(9) is 0, 1, 2, 3, ..., 8
            if board[r][c] == 0:
                 return (r,c) # row, col

    return None, None # if no spaces in the board are empty (or 0)



def is_valid(board, guess, row, col):
    # figures out whether guess at row/col is valid
    # return True if valid, return False otherwise

    # Check row
    row_value = board[row]
    if guess in row_value:
        return False

    # Check col
    col_value = board.transpose()[col] # for the col associated with the row index
    if guess in col_value:
        return False

    # Check 3x3 grid
    # We want to locate what 3x3 grid the row/col is located.
    # if row = 5, col = 7

    row_start = (row // 3) * 3  # 1 // 3 = 0, 5 // 3 = 1, 7 //3 = 2
    col_start = (col // 3) * 3  # multiply by three for the exact grid position. for instance if col = 5, col_start index is 5//3 = 1*3 = 3

    grid = board[row_start : row_start + 3, col_start : col_start + 3]
    if guess in grid:
        return False

    # if we get here, it means checks passes
    return True


def solve_sudoku(board):
    row, col = find_empty(board)

    # Step 1: check if there's any space left. If no space is left, then puzzle solved
    if row is None:
        return True

    # Step 2: if there is space to put our guess then we want to come up with a guess between 1 and 9
    for guess in range(1, 10):
        # Step 3: check if this is a valid guess
        if is_valid(board, guess, row, col):
            #  Step 3.1: if valid, place that guess on that row,col
            board[row][col] = guess

            # Step 3.2: recursively call our function to do steps 1-3 on next empty cell
            if solve_sudoku(board):
                return True

        # Step 4: if not valid or if guess does not solve the sudoku puzzle, then we need to backtrack
        # and try a new guess

        # Change row/col back to 0 (or an empty cell) because we did not successfully place
        # a number (between 1-9) there
        board[row][col] = 0


    # Step 5: if none of the numbers between 1-9 work, then sudoku puzzle is unsolvable
    return False

print("\n")
print_board(puzzle)
print(solve_sudoku(puzzle))
print("------------------------------\n")
print_board(puzzle)
print("\n")
