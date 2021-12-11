import math
from collections import deque, namedtuple

from aoc.utils import load_data, profiler

Grid = list[list[int]]
Rules = namedtuple("Rules", ["xr", "yr", "value"])


@profiler
def part1(data: Grid) -> int:
    mx = len(data[0]) - 1
    my = len(data) - 1
    risk_levels = []
    skip = False
    for y in range(my + 1):
        for x in range(mx + 1):
            if skip:
                skip = False
                continue
            point = data[y][x]
            x0 = 10 if x == 0 else data[y][x - 1]
            x1 = 10 if x == mx else data[y][x + 1]
            if point < min(x0, x1):
                if x != mx:
                    skip = True
                y0 = 10 if y == 0 else data[y - 1][x]
                y1 = 10 if y == my else data[y + 1][x]
                if point < min(y0, y1):
                    risk_levels.append(point + 1)
    return sum(risk_levels)


def walk(seed: tuple[int, int], grid: Grid, rules: Rules) -> int:
    size = 0
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    queue = deque([seed])
    while queue:
        y, x = queue.popleft()
        if grid[y][x] != -1:
            size += 1
            grid[y][x] = -1
            for dy, dx in dirs:
                nx = x + dx
                ny = y + dy
                if (
                    nx not in rules.xr
                    and ny not in rules.yr
                    and grid[ny][nx] not in rules.value
                ):
                    queue.append((ny, nx))
    return size


@profiler
def part2(data: Grid) -> int:
    mx = len(data[0])
    my = len(data)
    sizes = []
    rules = Rules((-1, mx), (-1, my), (-1, 9))
    for y in range(my):
        for x in range(mx):
            if data[y][x] not in rules.value:
                sizes.append(walk((y, x), data, rules))
    return math.prod(sorted(sizes)[-3:])


def main():
    data = load_data(test=False)
    data = [[int(x) for x in line] for line in data]
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
