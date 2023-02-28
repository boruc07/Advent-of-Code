import ast
from collections.abc import Iterable


def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


# Input text
with open("day13/input.txt", 'rt') as f:
    input_string = f.readlines()

pair_ind = 0
pair_dict = {}
for line in input_string:
    if line == "\n":
        pair_ind += 1
    else:
        if not pair_dict.get(pair_ind):
            pair_dict[pair_ind] = []
        line = line.replace("\n", "")
        pair_dict[pair_ind].append(ast.literal_eval(line))  # ast.literal_eval(line)

# Go through pairs and compare
right_order_sum = 0
is_right = True
for k, v in pair_dict.items():
    print("=========================")
    print(f"Item: {k} : {v}")
    left, right = v
    # left = list(flatten(left)) if isinstance(left, list) else left
    # right = list(flatten(right)) if isinstance(right, list) else right
    if len(left) == 0:
        print("Left = 0")
        is_right = True

    for pos, item in enumerate(zip(left, right)):
        item_left, item_right = item
        print(f"Processing {pos} -> {item_left} | {item_right}")

        if len(right) < len(left):
            print("Right shorter than Left")
            is_right = False
            break
        if pos+1 >= len(left) and pos+1 < len(right) or len(left) == 0:
            print("Left = 0 or left ended")
            is_right = True
            break

        if isinstance(item_left, list) and isinstance(item_right, list) and len(item_right) < len(item_left):
            print("Right shorter than Left")
            is_right = False
            break
        if isinstance(item_left, list) and isinstance(item_right, list) and (pos+1 >= len(item_left) and pos+1 < len(item_right) or len(item_left) == 0):
            print("Left = 0 or left ended")
            is_right = True
            break

        # if isinstance(item_left, list) and isinstance(item_right, list):
        #     print(f" {isinstance(item_left, list)} and {isinstance(item_right, list)} and {len(item_left)} > 0 and {len(item_right)} > 0")
        while isinstance(item_left, list) and isinstance(item_right, list) and len(item_left) > 0 and len(item_right) > 0:
            # print(f"{item_left} vs {item_right}")
            while isinstance(item_left[0], list) and len(item_left[0]) > 0:
                item_left = item_left[0]
                # print(f"new item_left = {item_left}")
            while isinstance(item_right[0], list) and len(item_right[0]) > 0:
                item_right = item_right[0]
            print(f"Items left loop as : {item_left}, {item_right}")

            # If both elements are ints compare
            if isinstance(item_left, int) and isinstance(item_right, int):
                print("both ints")
                if item_left > item_right:
                    is_right = False
                    break
            # If one element is int and another list just compare with first list element
            if isinstance(item_left, list) and isinstance(item_right, int):
                print("Right is not lists")
                if item_left[0] > item_right:
                    is_right = False
                    break
            # If one element is int and another list just compare with first list element
            if isinstance(item_left, int) and isinstance(item_right, list):
                print("Left is not lists")
                if item_left > item_right[0]:
                    is_right = False
                    break
            else:
                item_left = item_left[1:]
                item_right = item_right[1:]
                print(f"New values: {item_left} || {item_right}")

        # # If both elements are lists compare list items one by one
        # if isinstance(left[pos], list) and isinstance(right[pos], list):
        #     print("both lists")
        #     if len(right[pos]) < len(left[pos]):
        #         is_right = False
        #         break
        #     for num, cell in enumerate(item_left):
        #         if left[pos][num] > right[pos][num]:
        #             is_right = False
        #             break
        # # If both elements are ints compare
        if isinstance(item_left, int) and isinstance(item_right, int):
            print("both ints")
            if item_left > item_right:
                is_right = False
                break
        # If one element is int and another list just compare with first list element
        if isinstance(item_left, list) and isinstance(item_right, int):
            print("Right is not lists")
            if item_left[0] > item_right:
                is_right = False
                break
        # If one element is int and another list just compare with first list element
        if isinstance(item_left, int) and isinstance(item_right, list):
            print("Left is not lists")
            if item_left > item_right[0]:
                is_right = False
                break
    if is_right:
        print(f"k: {k} correct")
        right_order_sum += k+1

print(right_order_sum)
