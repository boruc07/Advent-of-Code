# Input text
with open("day8/input.txt", 'rt') as f:
    input_string = f.readlines()

# Parse into 2D list
tree_list = []
tree_visible_list = []
for line in input_string:
    line_list = []
    line_list[:0] = line.replace("\n", "")
    tree_list.append([int(item) for item in line_list])

# Initialize visibility tree
tree_visible_list = [[] for lst in tree_list]
[tree_visible_list[pos].append(1) for pos, lst in enumerate(tree_list) for item in lst]


counter = 0
size = len(tree_list)
for row_pos, tree_row in enumerate(tree_list):
    for col_pos, tree in enumerate(tree_row):
        # Every outter tree counts
        if row_pos == 0 or col_pos == 0 or row_pos == size - 1 or col_pos == size - 1:
            # tree_visible_list[row_pos][col_pos] = 1
            # outter cells cannot be best
            pass
        else:
            # Check Down
            is_visible = True
            temp_row_pos = row_pos + 1
            temp_col_pos = col_pos
            counter = 0
            while is_visible and temp_row_pos < size:
                if tree_list[row_pos][col_pos] <= tree_list[temp_row_pos][temp_col_pos]:
                    is_visible = False
                temp_row_pos += 1
                counter += 1

            tree_visible_list[row_pos][col_pos] *= counter

            # Check Up
            is_visible = True
            temp_row_pos = row_pos - 1
            temp_col_pos = col_pos
            counter = 0
            while is_visible and temp_row_pos >= 0:
                if tree_list[row_pos][col_pos] <= tree_list[temp_row_pos][temp_col_pos]:
                    is_visible = False
                temp_row_pos -= 1
                counter += 1

            tree_visible_list[row_pos][col_pos] *= counter

            # Check Right
            is_visible = True
            temp_row_pos = row_pos
            temp_col_pos = col_pos + 1
            counter = 0
            while is_visible and temp_col_pos < size:
                if tree_list[row_pos][col_pos] <= tree_list[temp_row_pos][temp_col_pos]:
                    is_visible = False
                temp_col_pos += 1
                counter += 1

            tree_visible_list[row_pos][col_pos] *= counter

            # Check Left
            is_visible = True
            temp_row_pos = row_pos
            temp_col_pos = col_pos - 1
            counter = 0
            while is_visible and temp_col_pos >= 0:
                if tree_list[row_pos][col_pos] <= tree_list[temp_row_pos][temp_col_pos]:
                    is_visible = False
                temp_col_pos -= 1
                counter += 1

            tree_visible_list[row_pos][col_pos] *= counter

# Flatten 2D list
flat_list = [item for sublist in tree_visible_list for item in sublist]

print(max(flat_list))
