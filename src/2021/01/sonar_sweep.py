from pathlib import Path


def part1(data):
    count = 0
    current = data[0]
    for depth in data:
        count += (depth > current)
        current = depth
    return count


def part2_slice(data):
    count = 0
    last_sum = sum(data[0:3])
    for i in range(1, len(data)-2):
        current_sum = sum(data[i:i+3])
        count += (current_sum > last_sum)
        last_sum = current_sum
    return count


def part2(data):
    count = 0
    window = [data.pop(0) for _ in range(3)]
    last_sum = sum(window)
    for depth in data:
        window.append(depth)
        window.pop(0)
        current_sum = sum(window)
        count += (current_sum > last_sum)
        last_sum = current_sum
    return count


if __name__ == "__main__":
    with open(Path(__file__).absolute().parent / "input.txt") as f:
        data = [int(depth) for depth in f.readlines()]
    print(part1(data), [part2_slice(data), part2(data)], sep="\n")
