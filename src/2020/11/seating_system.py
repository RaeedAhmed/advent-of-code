from itertools import product, chain
from copy import deepcopy
from collections import Counter, deque
from aoc.utils import load_data, profiler
import subprocess
import time


@profiler
def part1(grid: list[str]) -> None:
    dirs = list(product([-1, 0, 1], repeat=2))
    dirs.remove((0, 0))
    grid_tmp = deepcopy(grid)
    while True:
        xmax = len(grid[0])
        ymax = len(grid)
        change = False
        for y in range(ymax):
            for x in range(xmax):
                if grid[y][x] == ".":
                    continue
                elif grid[y][x] == "L":
                    neighbors = False
                    for dy, dx in dirs:
                        ny = y + dy
                        nx = x + dx
                        if (0 <= nx < xmax) and (0 <= ny < ymax):
                            if grid[ny][nx] == "#":
                                neighbors = True
                    if not neighbors:
                        grid_tmp[y][x] = "#"
                        change = True
                elif grid[y][x] == "#":
                    count = 0
                    for dy, dx in dirs:
                        ny = y + dy
                        nx = x + dx
                        if (0 <= nx < xmax) and (0 <= ny < ymax):
                            count += grid[ny][nx] == "#"
                    if count >= 4:
                        grid_tmp[y][x] = "L"
                        change = True
        if not change:
            break
        grid = deepcopy(grid_tmp)
    occupied = Counter(chain.from_iterable(grid))["#"]
    return occupied


@profiler
def part2(grid: list[list[str]]) -> None:
    dirs = list(product([-1, 0, 1], repeat=2))
    dirs.remove((0, 0))
    grid_tmp = deepcopy(grid)
    sight = deque()
    while True:
        xmax = len(grid[0])
        ymax = len(grid)
        change = False
        for y in range(ymax):
            for x in range(xmax):
                if grid[y][x] == ".":
                    continue
                elif grid[y][x] == "L":
                    neighbors = False
                    for dy, dx in dirs:
                        sight.clear()
                        for P in range(1, 9):
                            ny = y + P * dy
                            nx = x + P * dx
                            if (0 <= nx < xmax) and (0 <= ny < ymax):
                                sight.append(grid[ny][nx])
                            else:
                                break
                        while sight:
                            state = sight.popleft()
                            if state != ".":
                                if state == "#":
                                    neighbors = True
                                break
                    if not neighbors:
                        grid_tmp[y][x] = "#"
                        change = True
                elif grid[y][x] == "#":
                    count = 0
                    for dy, dx in dirs:
                        sight.clear()
                        for P in range(1, 9):
                            ny = y + P * dy
                            nx = x + P * dx
                            if (0 <= nx < xmax) and (0 <= ny < ymax):
                                sight.append(grid[ny][nx])
                            else:
                                break
                        while sight:
                            state = sight.popleft()
                            if state != ".":
                                if state == "#":
                                    count += 1
                                break
                    if count >= 5:
                        grid_tmp[y][x] = "L"
                        change = True
        if not change:
            break
        grid = deepcopy(grid_tmp)
        subprocess.call("clear")
        for row in grid:
            print("".join(row))
        time.sleep(.3)
    occupied = Counter(chain.from_iterable(grid))["#"]
    return occupied


def main():
    grid = [[seat for seat in row] for row in load_data(test=True)]
    grid_copy = deepcopy(grid)
    # print(part1(grid))
    print(part2(grid_copy))


if __name__ == "__main__":
    main()
