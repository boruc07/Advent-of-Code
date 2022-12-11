import re
# Input text
with open("day3/input.txt", 'rt') as f:
    input = f.read()

# Split into items
input_list = input.split("\n")

# Iterate through items if \n then it's another rucksack
sum = 0

for rucksack in input_list:
    first_comp = rucksack[:len(rucksack)//2]
    second_comp = rucksack[len(rucksack)//2:]
    common = ''.join(set(first_comp).intersection(second_comp))

    # Normalize priorities from ascii numbers
    if re.search("[a-z]",common):
        sum += ord(common) - 96

    else: # A-Z letters
        sum += ord(common) - 64 + 26
print(sum)