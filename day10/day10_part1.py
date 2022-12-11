# Input text
with open("day10/input.txt", 'rt') as f:
    input_string = f.readlines()

# Cycles required for operation
cycle_dict = {
    "noop": 1,
    "addx": 2,
}

x = 1
cycle_num = 0
signal_strength = 0

for instruction in input_string:
    instruction = instruction.replace("\n", "")

    # For every instruction iterate through cycles in order to calculate strength in correct moment
    for cycle in range(cycle_dict[instruction[:4]]):
        cycle_num += 1

        if cycle_num % 40 == 20:
            signal_strength += x * cycle_num
    if instruction[:4] == "addx":
        x += int(instruction[5:])

print(signal_strength)
