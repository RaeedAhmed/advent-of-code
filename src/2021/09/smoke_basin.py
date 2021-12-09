from aoc.utils import load_data, profiler


@profiler
def part1(data: list[list[int]]) -> int:
    mx = len(data[0]) - 1
    my = len(data) - 1
    risk_levels = []
    skip = False
    for y in range(my + 1):
        for x in range(mx + 1):
            point = data[y][x]
            x0 = 10 if x == 0 else data[y][x - 1]
            x1 = 10 if x == mx else data[y][x + 1]
            if point < min(x0, x1):
                y0 = 10 if y == 0 else data[y - 1][x]
                y1 = 10 if y == my else data[y + 1][x]
                if point < min(y0, y1):
                    risk_levels.append(point + 1)
    return sum(risk_levels)


@profiler
def part2() -> None:
    pass


def main():
    data = load_data(2021, 9, test=False)
    data = [[int(x) for x in line] for line in data]
    print(part1(data))


if __name__ == "__main__":
    main()
