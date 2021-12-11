from aoc.utils import load_data, profiler


@profiler
def part1(data: set[int]) -> int:
    for num in data:
        if (complement := 2020 - num) in data:
            return num * complement


@profiler
def part2(data: set[int]) -> int:
    for x in data:
        for num in data:
            if (complement := 2020 - x - num) in data:
                return x * num * complement


def main() -> None:
    data = set(map(int, load_data(test=False)))
    print(part1(data), part2(data))


if __name__ == "__main__":
    main()
