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
display = ""

for instruction in input_string:
    instruction = instruction.replace("\n", "")

    # For every instruction iterate through cycles
    for cycle in range(cycle_dict[instruction[:4]]):
        cycle_num += 1

        # CRT position starts from 0 for cycle 1
        crt_position = (cycle_num - 1) % 40
        sprite_pos = x
        pixel = "#" if abs(crt_position - sprite_pos) <= 1 else "."
        display += pixel

    if instruction[:4] == "addx":
        x += int(instruction[5:])


n = 40
display = [display[i:i+n] for i in range(0, len(display), n)]

for row in display:
    print(row)
# rehprlvb
# REHPRLUB
