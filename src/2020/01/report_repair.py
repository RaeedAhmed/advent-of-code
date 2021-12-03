from pathlib import Path


def part1(data: set[int]) -> int:
    for num in data:
        if (complement := 2020-num) in data:
            return num * complement


def part2(data: set[int]) -> int:
    for x in data:
        for num in data:
            if (complement := 2020-x-num) in data:
                return x * num * complement


def load_data(filename: str):
    with open(Path(__file__).absolute().parent / filename) as f:
        data = {int(depth) for depth in f.readlines()}
    return data


def test():
    data = load_data("test.txt")
    assert part1(data) == 514579
    assert part2(data) == 241861950
    print("\n***test passed***\n")


def run():
    data = load_data("input.txt")
    return part1(data), part2(data)


if __name__ == "__main__":
    test()
    p1, p2 = run()
    print(p1, p2, sep="\n")
