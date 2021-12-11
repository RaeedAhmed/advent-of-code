from dataclasses import dataclass

from aoc.utils import load_data, profiler


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


@profiler
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


@profiler
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
    data: list[Vector] = [Vector(*line.split(" ")) for line in load_data(test=False)]
    print(part1(data), part2(data), sep="\n")
