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
    Head, Tail = grid
    H_row_new, H_col_new = Head

    # Save previous Head position
    H_row, H_col = Head

    # Establish move of Head
    if command == "U":
        H_row_new = H_row + 1
    elif command == "D":
        H_row_new = H_row - 1
    elif command == "L":
        H_col_new = H_col - 1
    elif command == "R":
        H_col_new = H_col + 1
    Head = (H_row_new, H_col_new)

    # Iterate over every Tail element
    for pos, item in enumerate(Tail):
        T_row, T_col = item
        # For first Tail element closest knot i Head, for other position -1
        if pos == 0:
            Next_row, Next_col = H_row_new, H_col_new
        else:
            Next_row, Next_col = Tail[pos-1]

        if not areTouching(T_row, T_col, Next_row, Next_col):
            # Diagonal move
            if T_row != Next_row and T_col != Next_col:
                T_row += 1 if T_row < Next_row else -1
                T_col += 1 if T_col < Next_col else -1
            # Left / Right move
            elif T_row == Next_row and T_col != Next_col:
                T_col += 1 if T_col < Next_col else -1
            # Up / Down move
            elif T_row != Next_row and T_col == Next_col:
                T_row += 1 if T_row < Next_row else -1
            Tail[pos] = (T_row, T_col)
            # Check last Tail element if visited new position
            if pos == 8 and Tail[pos] not in visited_grid:
                visited_grid.add((T_row, T_col))
    return [Head, Tail]


# Define starting point and the grid setup (Head and Tail position)
Head = (0, 0)
Tail = [(0, 0) for item in range(9)]
grid = [Head, Tail]
# Acumulator for positions visited by Tail 8th element
visited_grid = {Tail[8]}


for command in input_string:
    # Iterate step by step ofer every instruction
    for iter in range(int(command[2:4].replace('\n', ''))):
        grid = moveHead(grid, visited_grid, command[0])
        command = command.replace('\n', '')

print(len(visited_grid))
