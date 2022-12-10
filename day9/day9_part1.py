# Input text
with open("day9/input.txt", 'rt') as f:
    input_string = f.readlines()


def gridPrint(grid: list):
    for item in grid:
        print(item)


def areTouching(T_row, T_col, H_row, H_col):
    if abs(H_row - T_row) <= 1 and abs(H_col - T_col) <= 1:
        return True
    else:
        return False


def moveHead(grid: list, visited_grid: set, command: str):
    T_row, T_col, H_row, H_col = grid
    H_row_new, H_col_new = grid[2:4]

    # Establish move of Head
    if command == "U":
        H_row_new = H_row + 1
    elif command == "D":
        H_row_new = H_row - 1
    elif command == "L":
        H_col_new = H_col - 1
    elif command == "R":
        H_col_new = H_col + 1
    # Tail can just take previous Head position if not adjacent anymore
    if not areTouching(T_row, T_col, H_row_new, H_col_new):
        T_row, T_col = H_row, H_col
        # Check Tail if visited new position
        if (T_row, T_col) not in visited_grid:
            visited_grid.add((T_row, T_col))
    return T_row, T_col, H_row_new, H_col_new


# Define starting point and the grid setup (Head and Tail position)
T_row, T_col, H_row, H_col = 0, 0, 0, 0
grid = [T_row, T_col, H_row, H_col]
# Acumulator for positions visited by Tail
visited_grid = {(T_row, T_col)}

for command in input_string:
    # Iterate step by step ofer every instruction
    for iter in range(int(command[2:4].replace('\n', ''))):
        grid = moveHead(grid, visited_grid, command[0])


print(len(visited_grid))
