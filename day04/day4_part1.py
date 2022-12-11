# Input text
with open("day4/input.txt", 'rt') as f:
    input_text = f.read()

# Split into items
input_list = input_text.split("\n")
counter = 0

for pair in input_list:
    first, second = pair.split(",")
    first = set(range(int(first.split("-")[0]), int(first.split("-")[1])+1))
    second = set(range(int(second.split("-")[0]), int(second.split("-")[1])+1))

    if first.issubset(second) or second.issubset(first):
        counter += 1

print(counter)
