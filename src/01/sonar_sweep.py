def part1(data):
    count = 0
    current = data[0]
    for depth in data:
        count += (depth > current)
        current = depth
    return count


def part2(data):
    count = 0
    for i in range(len(data)-3):
        count += (sum(data[i+1:i+4]) > sum(data[i:i+3]))
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [int(depth) for depth in f.readlines()]
    print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")
