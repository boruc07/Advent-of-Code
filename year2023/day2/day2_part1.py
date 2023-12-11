import re

def get_game_constraints():
    return {"red": 12,
            "green": 13,
            "blue": 14}

def _extract_input():
# Input text
    with open("year2023/day2/input1.txt", 'rt') as f:
        input = f.readlines()
    return input

def search_color(color, string):
    try:
        return int(re.search(rf"(\d+) {color}", string).group(1))
    except:
        return 0 

def parse_colors(string):
    blue = search_color('blue', string)
    red = search_color('red', string)
    green = search_color('green', string)
    return red, green, blue

def parse_game_number(string):
    try:
        return int(re.search(rf"Game (\d+):", string).group(1))
    except:
        pass 

def check_result(input):
    result = 0
    rules = get_game_constraints()
    for game in input:
        game_number = parse_game_number(game)
        for game_set in game.split(';'):
            red, green, blue = parse_colors(game_set)            
            if red > rules["red"] or green > rules["green"] or blue > rules["blue"]:
                game_number = 0
                break
        result += game_number

    return result

def main():
    input = _extract_input()
    result = check_result(input)
    print(result)


if __name__== '__main__':
    main()