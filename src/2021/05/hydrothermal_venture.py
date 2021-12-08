from collections import Counter

from aoc.utils import load_data, profiler


@profiler
def main():
    counter = Counter()
    data = load_data(2021, 5, test=False)
    for line in data:
        c1, c2 = line.split(" -> ")
        x0, y0 = map(int, c1.split(","))
        x1, y1 = map(int, c2.split(","))
        if x0 == x1:
            counter.update((x0, y) for y in range(min(y0, y1), max(y0, y1) + 1))
        elif y0 == y1:
            counter.update((x, y0) for x in range(min(x0, x1), max(x0, x1) + 1))
        elif abs(x1 - x0) == abs(y1 - y0):
            xi = 1 if x1 > x0 else -1
            yi = 1 if y1 > y0 else -1
            counter.update((x0 + i * xi, y0 + i * yi) for i in range(abs(x1 - x0) + 1))
    print(sum(count > 1 for count in counter.values()))


if __name__ == "__main__":
    main()
