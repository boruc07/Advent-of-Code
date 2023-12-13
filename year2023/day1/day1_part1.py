def _extract_input():
# Input text
    with open("year2023/day1/input1.txt", 'rt') as f:
        input = f.readlines()
    return input


def main():
    input = _extract_input()
    result = 0
    for line in input:
        for char in line:
            if char.isnumeric():
                first = char
                break
        for char in reversed(line):
            if char.isnumeric():
                last = char
                break
        result = result + int(first+last)
    print(result)


if __name__== '__main__':
    main()