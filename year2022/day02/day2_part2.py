# Input text
with open("day2/input.txt", 'rt') as f:
    input = f.read()

# Rules book
rules_dict = {
    "X": "loose",
    "Y": "draw",
    "Z": "win",
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

# Get shape for win or loose based on opponent's shape
strategy_dict = {
    "win": {"R":"P",
            "P":"S",
            "S":"R"},
    "loose": {"P":"R",
            "S":"P",
            "R":"S"}
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

    if me == "draw":
        game_points += game_score_dict["draw"] + shape_dict[opponent]
    elif me == "win":
        game_points += game_score_dict["win"] + shape_dict[strategy_dict["win"][opponent]]
    elif me == "loose":
        game_points += game_score_dict["loose"] + shape_dict[strategy_dict["loose"][opponent]]
    
print(game_points)