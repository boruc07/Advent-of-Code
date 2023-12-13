class Day4():

    def __init__(self) -> None:
        self.input = None
        self.length = None

    def extract_input(self):
        # Input text
        with open("year2023/day4/input1.txt", 'rt') as f:
            self.input = f.readlines()
            self.length = len(self.input)

    def _parse_winning_numbers(self, winning_numbers):
        # Remove "Card N: " part
        winning_numbers = winning_numbers.split(":")[1]
        # Split numbers
        winning_numbers = winning_numbers.split(" ")
        # Clean empty elements caused by extra spaces
        winning_numbers = [i for i in winning_numbers if i != '']
        return winning_numbers

    def _parse_game_numbers(self, game_numbers):
        game_numbers = game_numbers.replace("\n", "")
        # Split numbers
        game_numbers = game_numbers.split(" ")
        # Clean empty elements caused by extra spaces
        game_numbers = [i for i in game_numbers if i != '']
        return game_numbers

    def parse_games(self):
        games = []
        for game in self.input:
            game_set = game.split(" | ")
            winning_numbers = game_set[0]
            game_numbers = game_set[1]

            winning_numbers = self._parse_winning_numbers(winning_numbers)
            game_numbers = self._parse_game_numbers(game_numbers)

            games.append((winning_numbers, game_numbers))
        return games

    def calculate_score(self, games):
        score = 0
        for winning_numbers, game_numbers in games:
            matches = set(winning_numbers) & set(game_numbers)
            match_count = len(matches)
            match_score = pow(2, match_count-1) if match_count > 0 else 0
            score += match_score
        return score

    def run(self):
        self.extract_input()
        games = self.parse_games()
        print(self.calculate_score(games))


cl = Day4()
cl.run()
