from nis import match
import re
from functools import reduce

class Day3():

    def __init__(self) -> None:
        self.identified_set = set()

    def _extract_input(self):
    # Input text
        with open("year2023/day3/input1.txt", 'rt') as f:
            self.input = f.readlines()
            self.length = len(self.input)

    def find_symbols_positions(self):
        pattern = r"[^\w\d.\n]"
        symbols = set()
        for pos, line in enumerate(self.input):
            matches = [(m.start(), pos) for m in re.finditer(pattern, line)]
            for match in matches:            
                symbols.add(match)
        return symbols

    def pos_exists(self, x ,y):
        if x < 0 or y < 0 or x >= self.length or y >= self.length or (x,y) in self.identified_set:
            return False
        return True

    def find_number(self, x, y):
        if not self.pos_exists(x ,y):
            return None, None, None  
          
        number = self.input[y][x]

        if not number.isnumeric():
            return None, None, None    

        iter=1
        max_x, min_x = x, x
        while self.pos_exists(x-iter,y) and self.input[y][x-iter].isnumeric():
            number = self.input[y][x-iter] + number
            min_x = x-iter
            iter+=1
        iter=1
        
        while self.pos_exists(x+iter,y) and self.input[y][x+iter].isnumeric():
            number = number + self.input[y][x+iter]
            max_x = x+iter
            iter+=1

        return number, min_x, max_x

    def mark_identified_number(self, min_x, max_x, y):
        for x in range(min_x, max_x+1):
            self.identified_set.add((x,y))

    def identify_adjacent_numbers(self, symbols):
        numbers = []   
           
        for x, y in symbols:
            temp_numbers = []  
            is_gear = True if self.input[y][x] == '*' else False
            match_count = 0
            for x_mod, y_mod in [(x,y) for x in range(-1,2) for y in range(-1,2)]:
                number, min_x, max_x = self.find_number(x+x_mod, y+y_mod)
                
                if number:
                    match_count += 1
                    temp_numbers.append(int(number))
                    self.mark_identified_number(min_x, max_x, y+y_mod)
            if is_gear and match_count == 2:
                number = reduce(lambda x, y: x*y, temp_numbers)
                numbers.append(number)
        return numbers




    def run(self):
        self._extract_input()
        symbols = self.find_symbols_positions()
        numbers = self.identify_adjacent_numbers(symbols)
        print(sum(numbers))

cl = Day3()
cl.run()