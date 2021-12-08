import statistics

from aoc.utils import load_data, profiler


@profiler
def part1(data: list[int]) -> int:
    median = statistics.median(data)
    start = int(median - 0.5)
    end = int(median + 0.5)
    minimum = sum(data)
    for i in range(start, end):
        current = sum([abs(num - i) for num in data])
        if current < minimum:
            minimum = current
    return minimum


@profiler
def part2(data: list[int]):
    minimum = 999999999
    mean = statistics.mean(data)
    start = int(mean - 0.5)
    end = int(mean + 0.5)
    data_max = max(data)
    s = {0: 0, 1: 1}
    for i in range(2, data_max):
        s[i] = s[i - 1] + i
    for i in range(start, end):
        current = sum([s[abs(num - i)] for num in data])
        if current < minimum:
            minimum = current
    return minimum


def main():
    data = list(map(int, load_data(2021, 7, test=False)[0].split(",")))
    print(part1(data))  # 0.000183s
    print(part2(data))  # 0.000992s


if __name__ == "__main__":
    main()
