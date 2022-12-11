import re

# Input text
with open("day5/input_crates.txt", 'rt') as f:
    input_crates = f.readlines()

# Declare temporary lists
crates = []
crate = []
column_crates = []

# Add empty crates in order to normalize data
input_crates = [line.replace("    ", "[ ] ").replace(
    "     ", " [ ] ") for line in input_crates]

# Find creates in lists
for line in input_crates:
    [crate.append(item) for item in re.findall('\[.\]', line)]
    crates.append(crate)
    crate = []

# Rearrange crates, every column is another list
for pos in range(9):
    [crate.append(item[pos]) for item in crates]
    column_crates.append(crate)
    crate = []

# Remove empty crates
crates = []
for crate in column_crates:
    crates.append([item for item in crate if item != "[ ]"])

# Input text
with open("day5/input_procedure.txt", 'rt') as f:
    input_text = f.read()
# Split into items
input_list = input_text.split("\n")

for procedure in input_list:
    steps = re.findall("[0-9]+", procedure)
    amount = int(steps[0])
    from_c = int(steps[1]) - 1
    to_c = int(steps[2]) - 1

    # Can only move as many elements as there are in a list
    if amount > len(crates[from_c]):
        amount = len(crates[from_c])

    # do nothing if there is nothing to move or if moving to the same stack
    if len(crates[from_c]) > 0 and to_c != from_c:
        # Add crates to destination stack in reversed order
        crates[to_c] = list(reversed(crates[from_c][:amount])) + crates[to_c]
        # Delete crates from source stack
        crates[from_c] = crates[from_c][amount:]

output = ""
for row in crates:
    print(*row)
    output += (row[0].replace("[", "").replace("]", ""))
print(output)
