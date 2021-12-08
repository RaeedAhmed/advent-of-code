from aoc.utils import load_data, profiler


@profiler
def part1(data: list[str]) -> None:
    container = set()
    count = 0
    for line in data:
        if not line:
            count += len(container)
            container.clear()
        container.update(line)
    print(count)


@profiler
def part2(data: list[str]) -> None:
    group = []
    count = 0
    clear = False
    for line in data:
        if not line:
            count += len(set.intersection(*group))
            group.clear()
            clear = True
        if not clear:
            group.append(set(line))
        if clear:
            clear = False
    print(count)


def main() -> None:
    data = load_data(2020, 6, test=False) + [""]
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
