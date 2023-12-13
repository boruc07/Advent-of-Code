class Day4():

    def __init__(self) -> None:
        self.input = None
        self.length = None
        self.copies_accumulator = {}

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

    def calculate_games(self, games):
        for pos, (winning_numbers, game_numbers) in enumerate(games):
            card_copy_count = self.copies_accumulator[pos] if pos in self.copies_accumulator else 0
            matches = set(winning_numbers) & set(game_numbers)
            match_count = len(matches)
            # match_score = pow(2, match_count-1) if match_count > 0 else 0
            if match_count > 0:
                for number in range(1, match_count+1):
                    if pos + number in self.copies_accumulator:
                        new_value = self.copies_accumulator[pos+number] + 1 + card_copy_count
                    else:
                        new_value = 1 + card_copy_count
                    self.copies_accumulator[pos+number] = new_value

        # return score
    def count_cards(self, games):
        cards_number = 0
        for copy_count in self.copies_accumulator.values():
            cards_number += copy_count
        return cards_number + len(games)

    def run(self):
        self.extract_input()
        games = self.parse_games()
        self.calculate_games(games)
        count = self.count_cards(games)
        print(count)


cl = Day4()
cl.run()
