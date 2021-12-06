from pathlib import Path


def part1(data: list[str]):
    container = set()
    count = 0
    for line in data:
        if not line:
            count += len(container)
            container.clear()
        container.update(line)
    print(count)


def part2(data: list[str]):
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


def main(filename: str):
    with open(Path(__file__).absolute().parent / filename) as f:
        data = [line.strip() for line in f.readlines()] + [""]
    part1(data)
    part2(data)


if __name__ == "__main__":
    for filename in ["test.txt", "input.txt"]:
        main(filename)
