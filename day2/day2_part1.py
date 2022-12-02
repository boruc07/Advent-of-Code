# Input text
with open("day2/input.txt", 'rt') as f:
    input = f.read()

# Rules book
rules_dict = {
    "X": "R",
    "Y": "P",
    "Z": "S",
    "A": "R",
    "B": "P",
    "C": "S",
}

# Shape score
shape_dict = {
    "R": 1,
    "P": 2,
    "S": 3,
}

# Game score
game_score_dict ={
    "win": 6,
    "loose": 0,
    "draw": 3,
}

# Map values to universal R, P, S
for word, replacement in rules_dict.items():
    input = input.replace(word, replacement)

# Split into items
games_list = input.split("\n")
game_points = 0

# List through games, calculate score
for game in games_list:
    opponent, me = game.split(" ")

    if opponent == me:
        game_points += game_score_dict["draw"] + shape_dict[me]
    elif game == "R P" or game == "P S" or game == "S R":
        game_points += game_score_dict["win"] + shape_dict[me]
    elif game == "P R" or game == "S P" or game == "R S":
        game_points += game_score_dict["loose"] + shape_dict[me]
    
print(game_points)