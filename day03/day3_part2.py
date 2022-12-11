import re
# Input text
with open("day3/input.txt", 'rt') as f:
    input = f.read()

# Split into items
input_list = input.split("\n")

sum = 0
# Zip lines in a groups of three
for e1, e2, e3 in  zip(*[iter(input_list)]*3):   
    common = ''.join(set(e1).intersection(e2,e3))

    # Normalize priorities from ascii numbers
    if re.search("[a-z]",common):
        sum += ord(common) - 96

    else: # A-Z letters
        sum += ord(common) - 64 + 26
print(sum)