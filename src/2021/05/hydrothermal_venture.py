from collections import Counter
from pathlib import Path


def main(filename: str):
    counter = Counter()
    with open(Path(__file__).absolute().parent / filename) as f:
        data = [line.strip() for line in f.readlines()]
    for line in data:
        c1, c2 = line.split(" -> ")
        x0, y0 = map(int, c1.split(","))
        x1, y1 = map(int, c2.split(","))
        if x0 == x1:
            counter.update((x0, y)
                           for y in range(min(y0, y1), max(y0, y1) + 1))
        elif y0 == y1:
            counter.update((x, y0)
                           for x in range(min(x0, x1), max(x0, x1) + 1))
        elif abs(x1-x0) == abs(y1-y0):
            xi = 1 if x1 > x0 else -1
            yi = 1 if y1 > y0 else -1
            counter.update((x0+i*xi, y0+i*yi) for i in range(abs(x1-x0) + 1))
    return sum(count > 1 for count in counter.values())


if __name__ == "__main__":
    for filename in ["test.txt", "input.txt"]:
        print(main(filename))
