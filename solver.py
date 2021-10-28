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
