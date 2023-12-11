digit_mapping = {
'one': '1',
'two': '2',
'three': '3',
'four': '4',
'five': '5',
'six': '6',
'seven': '7',
'eight': '8',
'nine': '9',
}

def _extract_input():
    with open("year2023/day1/input1.txt", 'rt') as f:
        input = f.readlines()
    return input

def find_literal(text):
    for literal, digit in digit_mapping.items():
        if text.find(literal) != -1:
            return digit
    return False

def identify_first_digit(line):
    char_buffer=''
    for char in line:
        char_buffer=char_buffer+char
        if char.isnumeric():
            return char            
        elif find_literal(char_buffer):
            return find_literal(char_buffer)

def identify_last_digit(line):
    char_buffer=''
    for char in reversed(line):
        char_buffer=char+char_buffer
        if char.isnumeric():
            return char            
        elif find_literal(char_buffer):
            return find_literal(char_buffer)


def main():
    input = _extract_input()    
    result = 0

    for line in input:
        first = identify_first_digit(line)
        last = identify_last_digit(line)                
        result = result + int(first+last)
    print(result)

if __name__== '__main__':
    main()