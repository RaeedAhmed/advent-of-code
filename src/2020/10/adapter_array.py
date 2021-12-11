import math
from collections import deque
from itertools import groupby

from aoc.utils import load_data, profiler


@profiler
def part1(queue: deque[int]) -> int:
    counter = {1: 0, 3: 0}
    previous = 0
    queue.append(max(queue) + 3)
    while queue:
        cursor = queue.popleft()
        counter[cursor - previous] += 1
        previous = cursor
    return counter[1] * counter[3]


@profiler
def part2(queue: deque[int]) -> int:
    queue.append(max(queue) + 3)
    differences = []
    previous = 0
    while queue:
        cursor = queue.popleft()
        differences.append(cursor - previous)
        previous = cursor
    return math.prod(
        (2 ** (len(m) - 1)) - (len(m) == 4)
        for k, g in groupby(differences)
        if k == 1 and len((m := list(g))) > 1
    )


def main():
    data = sorted(list(map(int, load_data(test=False))))
    print(part1(deque(data)))
    print(part2(deque(data)))


if __name__ == "__main__":
    main()
