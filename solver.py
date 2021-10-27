board = [[0 for i in range(9)] for j in range(9)]

def print_grid(grid):
    for idx, row in enumerate(grid):
        if (idx) % 3 == 0:
            print("-"*20)
        print("| " + " ".join(str(elem) for elem in row) + " |")
    print("-"*20)

print_grid(board)
