from pathlib import Path


def part1(data):
    count = 0
    current = data[0]
    for depth in data:
        count += (depth > current)
        current = depth
    return count


def part2_old(data):
    count = 0
    for i in range(len(data)-3):
        count += (sum(data[i+1:i+4]) > sum(data[i:i+3]))
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
    print(part1(data), part2(data), sep="\n")
