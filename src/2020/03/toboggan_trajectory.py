from dataclasses import dataclass

from aoc.utils import load_data, profiler


@dataclass
class Position:
    x: int
    y: int


@profiler
def main() -> None:
    data = load_data(test=False)
    width = len(data[0])
    product = 1
    for x, y in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        count = 0
        pos = Position(0, 0)
        for _ in range(int(len(data) / y) - 1):
            pos.x += x
            pos.x %= width
            pos.y += y
            count += data[pos.y][pos.x] == "#"
        product *= count
    print(product)


if __name__ == "__main__":
    main()
