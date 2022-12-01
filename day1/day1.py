# Input text
with open("input.txt", 'rt') as f:
    input = f.read()

# Split into items
input_list = input.split("\n")

# Iterate through items if \n then it's another elf
sum_list = []
iterator = 0
sum_value = 0

for item in input_list:
    if item != "":
        sum_value += int(item)
    else:
        iterator += 1
        sum_list.append(sum_value)
        sum_value = 0

# Get top3 values
top3 = sorted(sum_list, reverse=True)[:3]

print(max(sum_list)) # 1st task
print(sum(top3)) # 2nd task