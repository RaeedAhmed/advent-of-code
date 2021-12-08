from aoc.utils import load_data, profiler
from itertools import combinations
from collections import deque

PLEN = 25


@profiler
def part1(preamble: deque[int], queue: deque[int]) -> int:
    while queue:
        num = queue.popleft()
        sums = [x+y for x, y in combinations(preamble, 2)]
        if num in sums:
            preamble.popleft()
            preamble.append(num)
        else:
            return num


@profiler
def part2(data: list[int], invalid: int) -> None:
    n = 1
    while True:
        for i in range(len(data) - n):
            if invalid == sum(data[i:i+n+1]):
                s = sorted(data[i:i+n+1])
                return s[0] + s[-1]
        n += 1


def main():
    data = list(map(int, load_data(2020, 9, test=False)))
    preamble = deque(data[:PLEN])
    queue = deque(data[PLEN:])
    invalid = part1(preamble, queue)
    print(invalid, part2(data, invalid))


if __name__ == "__main__":
    main()
