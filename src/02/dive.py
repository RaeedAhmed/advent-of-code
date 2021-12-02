from typing import NamedTuple
from dataclasses import dataclass


class Vector(NamedTuple):
    direction: str
    magnitude: int


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
    with open("input.txt") as f:
        raw: list[list[str]] = [line.split(" ") for line in f.readlines()]
        data: list[Vector] = [Vector(d, int(m)) for d, m in raw]
    print(part1(data), part2(data), sep="\n")
