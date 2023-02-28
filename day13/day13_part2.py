from collections.abc import Iterable


def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


left, right = [[[[]]], [[]]]

print(len(left[0]), len(right[0]))
