#!/usr/bin/env python3


def print_grid(grid):
    for idx, row in enumerate(grid):
        if idx % 3 == 0:
            print("|{}|".format("-" * 35))
        print("| " + " | ".join(" " if elem == 0 else str(elem)
              for elem in row) + " |")
    print("|{}|".format("-" * 35))


def make_grid(grid_str: str) -> list[list[int]]:
    """Creates sudoku board from string"""
    return [list(map(int, line)) for line in grid_str.replace(' ', '').splitlines()]


def get_row(i : int, board): -> list[int]:
    """Gets the row as a list from index i"""
    return board[i]

def get_col(j : int, board): -> list[int]:
    """Gets the column as a list from index j"""
    return [row[j] for row in board]


def valid_placement(value: int, i: int, j: int, board) -> Bool:
    """Validates whether the number represented by value can be placed at the given position"""

    # Checks row
    if any(x == value for x in get_row(i, board)):
        return False
    
    # Checks column
    if any(x == value for x in get_col(j, board)):
        return False


string = """043080250
            600000000
            000001094
            900004070
            000608000
            010200003
            820500000
            000000005
            034090710"""
print_grid(make_grid(string))
