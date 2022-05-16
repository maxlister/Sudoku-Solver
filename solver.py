#!/usr/bin/env python3
from itertools import chain


def print_grid(grid):
    for idx, row in enumerate(grid):
        if idx % 3 == 0:
            print("|{}|".format("-" * 35))
        print("| " + " | ".join(" " if elem == 0 else str(elem) for elem in row) + " |")
    print("|{}|".format("-" * 35))


def make_grid(grid_str: str) -> list[list[int]]:
    """Creates sudoku board from string"""
    return [list(map(int, line)) for line in grid_str.replace(' ', '').splitlines()]


def get_row(i: int, board) -> list[int]:
    """Gets the row as a list from index i"""
    return board[i]

def get_col(j: int, board) -> list[int]:
    """Gets the column as a list from index j"""
    return [row[j] for row in board]


def get_box(i: int, j: int, board) -> list[list[int]]:
    """Gets the sub-box containing the position represented by (i, j), for example
    (5, 2) is a coordinate within the row 2 column 1 sub-box so the function would return
    the elements of this sub-box
    """

    box_row = i // 3
    box_col = j // 3

    col_span = 3 * box_col

    return [board[3 * box_row][col_span: col_span + 3],
            board[3 * box_row + 1][col_span: col_span + 3],
            board[3 * box_row + 2][col_span: col_span + 3]]


def valid_placement(value: int, i: int, j: int, board) -> bool:
    """Validates whether the number represented by value can be placed at the given position"""

    # Checks row
    if any(x == value for x in get_row(i, board)):
        return False


    # Checks column
    if any(x == value for x in get_col(j, board)):
        return False

    # Checks sub-box
    sub_box = get_box(i, j, board)
    if any(x == value for x in chain(*sub_box)):
        return False

    return True

def find_first_zero(board) -> (int, int):
    """Goes through board row-wise and finds the first cell which is zero"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

    return -1, -1 # if all cells filled


def backtrack_solve(board) -> (bool, list[list[int]]):
    """
    Recursively solves the sudoku using brute-force backtracking
    The function starts with an unfilled cell and attempts to fill it with any valid number, then
    calls backtrack_solve on the new board, this continues until either the board is filled or no numbers can
    be placed without causing a contradiction, whence the function will return False
    """

    # Find a zero cell
    i, j = find_first_zero(board)
    if i == j == -1:
        return True, board # the board is solved

    for num in range(1, 10):
        if valid_placement(num, i, j, board):
            board[i][j] = num

            success, modified_board = backtrack_solve(board)
            if success:
                return True, modified_board

            # otherwise we reset our attempt
            board[i][j] = 0

    return False, board


string = """043080250
            600000000
            000001094
            900004070
            000608000
            010200003
            820500000
            000000005
            034090710"""

grid = make_grid(string)
# print_grid(grid)

success, solved = backtrack_solve(grid)
print_grid(solved)
