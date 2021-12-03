from dataclasses import dataclass
from pathlib import Path


@dataclass
class Vector:
    direction: str
    magnitude: int

    def __post_init__(self):
        self.magnitude = int(self.magnitude)


@dataclass
class Position:
    x: int = 0
    y: int = 0
    aim: int = 0

    def product(self):
        return self.x * self.y


def part1(data: list[Vector]) -> int:
    position = Position()
    for vector in data:
        if vector.direction == "forward":
            position.x += vector.magnitude
        elif vector.direction == "down":
            position.y += vector.magnitude
        else:
            position.y -= vector.magnitude

    return position.product()


def part2(data: list[Vector]) -> int:
    position = Position()
    for vector in data:
        if vector.direction == "forward":
            position.x += vector.magnitude
            position.y += position.aim * vector.magnitude
        elif vector.direction == "down":
            position.aim += vector.magnitude
        else:
            position.aim -= vector.magnitude

    return position.product()


if __name__ == "__main__":
    with open(Path(__file__).absolute().parent / "input.txt") as f:
        data: list[Vector] = [Vector(*line.split(" "))
                              for line in f.readlines()]
    print(part1(data), part2(data), sep="\n")
