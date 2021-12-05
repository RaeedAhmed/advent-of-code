from dataclasses import dataclass
from pathlib import Path


@dataclass
class Point:
    x: int
    y: int


class Coordinates:
    def __init__(self, line: str) -> None:
        coords = line.split(" -> ")
        x, y = coords[0].split(",")
        self.p1 = Point(int(x), int(y))
        x, y = coords[1].split(",")
        self.p2 = Point(int(x), int(y))


def main(filename: str):
    with open(Path(__file__).absolute().parent / filename) as f:
        data = [Coordinates(line.strip()) for line in f.readlines()]

    counter = {(x, y): 0 for x in range(999) for y in range(999)}
    for c in data:
        if c.p1.x == c.p2.x:
            d = c.p2.y - c.p1.y
            dir = int(d/abs(d))
            for y in range(c.p1.y, c.p2.y + dir, dir):
                counter[(c.p1.x, y)] += 1
        elif c.p1.y == c.p2.y:
            d = c.p2.x - c.p1.x
            dir = int(d/abs(d))
            for x in range(c.p1.x, c.p2.x + dir, dir):
                counter[(x, c.p1.y)] += 1
        elif abs(c.p2.x - c.p1.x) == abs(c.p2.y - c.p1.y):
            xi = c.p2.x - c.p1.x
            yi = c.p2.y - c.p1.y
            xd = int(xi/abs(xi))
            yd = int(yi/abs(yi))
            for i in range(abs(xi) + 1):
                counter[(c.p1.x + xd*i, c.p1.y + yd*i)] += 1

    print(len([v for v in counter.values() if v >= 2]))


if __name__ == "__main__":
    for filename in ["input.txt"]:
        main(filename)
