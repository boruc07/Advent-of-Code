# Input text
with open("day6/input.txt", 'rt') as f:
    input_string = f.read()

match_set = ()

# Go through characters, put into set if set of 4 is 4 long then all characters are distinct
how_many_distinct = 4
for pos in range(len(input_string)):
    if pos > how_many_distinct:
        match_set = set(input_string[pos-how_many_distinct:pos])
    if len(match_set) == how_many_distinct:
        break
print(pos)
