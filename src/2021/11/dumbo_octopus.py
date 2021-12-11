from itertools import product

from aoc.utils import load_data, profiler

Grid = dict[complex, int]


def flash(grid: Grid, flashed: set[complex], coord: complex, dirs: list[tuple]):
    flashed.add(coord)

    grid[coord] = -1
    for dy, dx in dirs:
        ncoord = coord + complex(dy, dx)
        if ncoord not in grid:
            continue
        grid[ncoord] += 1
        if grid[ncoord] > 9:
            flash(grid, flashed, ncoord, dirs)


@profiler
def run(grid: Grid, part: int) -> int:
    dirs = list(product([-1, 0, 1], repeat=2))
    dirs.remove((0, 0))
    total_flashed = 0
    steps = 100 if part == 1 else 10000
    for step in range(1, steps + 1):
        for coord in grid:
            grid[coord] += 1
        flashed: set[complex] = set()
        for coord, energy in grid.items():
            if energy > 9:
                flash(grid, flashed, coord, dirs)
        for coord in flashed:
            grid[coord] = 0
        if part == 1:
            total_flashed += len(flashed)
        elif len(flashed) == len(grid):
            return step
    return total_flashed


@profiler
def part2() -> None:
    pass


def main():
    data = load_data(test=False)
    grid = {
        complex(y, x): int(value)
        for y, row in enumerate(data)
        for x, value in enumerate(row)
    }
    tmp = grid.copy()
    print(run(grid, part=1))
    grid = tmp.copy()
    print(run(grid, part=2))


if __name__ == "__main__":
    main()
