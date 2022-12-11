import re


# Input text
with open("day11/input.txt", 'rt') as f:
    input_string = f.read()


class Monkey():
    def __init__(self, number: int, items: list, operation: str, test_number: str, if_true: int, if_false: int):
        self.number = number
        self.items = items
        self.operation = operation
        self.test_number = test_number
        self.if_true = if_true
        self.if_false = if_false
        self.items_inspected = 0

    def __repr__(self):
        return f"""Number: {self.number}
Items: {self.items}
Operation: {self.operation}
Test_number: {self.test_number}
If True: {if_true}
If False: {if_false}
Items_inspected : {self.items_inspected}"""

    def applyOperation(self, modulo: int) -> None:
        new_items = []
        for item in self.items:
            operation = self.operation.replace("old", str(item))

            # Apply calculation of new worry level
            new_item = eval(operation)

            # Apply modulo in order to maintain numbers correct
            # , as it's multiplication of denominators it won't interfere with test results
            new_item %= modulo

            new_items.append(new_item)
            self.items_inspected += 1
        self.items = new_items


def throwItems(monkey: Monkey, monkey_dict: dict):
    for item in monkey.items:
        if item % monkey.test_number == 0:
            monkey_dict[monkey.if_true].items.append(item)
        else:
            monkey_dict[monkey.if_false].items.append(item)
    monkey.items = []


def parseMonkeyText(monkey_text: str):
    items = re.search("Starting items: (.*)\n", monkey_text).group(1).split(", ")
    # Convert to int
    items = [int(x) for x in items]
    number = int(re.search("Monkey (.*):", monkey_text).group(1))
    operation = re.search("Operation: new = (old .*)\n", monkey_text).group(1)
    test_number = int(re.search("Test: divisible by (.*)\n", monkey_text).group(1))
    if_true = int(re.search("If true: throw to monkey (.*)\n", monkey_text).group(1))
    if_false = int(re.search("If false: throw to monkey (.*)$", monkey_text).group(1))

    return items, number, operation, test_number, if_true, if_false


# Dict for Monkey objects
monkey_dict = {}

input_string = input_string.split("\n\n")

# Generate monkeys
for monkey_text in input_string:
    items, number, operation, test_number, if_true, if_false = parseMonkeyText(monkey_text)
    monkey_dict[number] = Monkey(number, items, operation, test_number, if_true, if_false)

# In order to maintain numbers within calculable range, worry level must be lowered
# by applying modulo of multiplied denominators from all of Monkeys' tests
modulo = 1
for key, monkey in monkey_dict.items():
    modulo *= monkey.test_number


# Play 10000 rounds
for round in range(10000):
    for key, monkey in monkey_dict.items():
        monkey.applyOperation(modulo)
        throwItems(monkey, monkey_dict)

# Get monkey bussines after game
monkey_bussines = []
for key, item in monkey_dict.items():
    monkey_bussines.append(item.items_inspected)

# Pick two biggest values
largest_integer = max(monkey_bussines)
monkey_bussines.remove(largest_integer)
second_largest_integer = max(monkey_bussines)

print(largest_integer * second_largest_integer)
