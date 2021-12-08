from collections import deque

from aoc.utils import load_data, profiler


@profiler
def part1(data):
    count = 0
    current = data[0]
    for depth in data:
        count += depth > current
        current = depth
    return count


@profiler
def part2_slice(data):
    count = 0
    last_sum = sum(data[0:3])
    for i in range(1, len(data) - 2):
        current_sum = sum(data[i : i + 3])
        count += current_sum > last_sum
        last_sum = current_sum
    return count


@profiler
def part2(data: deque[int]):
    count = 0
    window = deque([data.popleft() for _ in range(3)])
    last_sum = sum(window)
    while data:
        window.append(data.popleft())
        window.popleft()
        current_sum = sum(window)
        count += current_sum > last_sum
        last_sum = current_sum
    return count


def main() -> None:
    data = list(map(int, load_data(2021, 1, test=False)))
    print(part1(deque(data)), part2_slice(data), part2(deque(data)), sep="\n")


if __name__ == "__main__":
    main()
