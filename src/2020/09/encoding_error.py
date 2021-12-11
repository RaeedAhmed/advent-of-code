from collections import deque
from itertools import combinations

from aoc.utils import load_data, profiler

PLEN = 25


@profiler
def part1(preamble: deque[int], queue: deque[int]) -> int:
    while queue:
        num = queue.popleft()
        sums = [x + y for x, y in combinations(preamble, 2)]
        if num in sums:
            preamble.popleft()
            preamble.append(num)
        else:
            return num


@profiler
def part2(data: list[int], invalid: int) -> int:
    for n in range(len(data) - 1):
        for i in range(len(data) - n):
            if invalid == sum(data[i : i + n + 1]):
                s = sorted(data[i : i + n + 1])
                return s[0] + s[-1]


def main():
    data = list(map(int, load_data(test=False)))
    preamble = deque(data[:PLEN])
    queue = deque(data[PLEN:])
    invalid = part1(preamble, queue)
    print(invalid, part2(data, invalid))


if __name__ == "__main__":
    main()
