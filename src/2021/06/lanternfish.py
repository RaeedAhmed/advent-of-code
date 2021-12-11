from pathlib import Path

from aoc.utils import load_data, profiler


@profiler
def main():
    data = list(map(int, (load_data(test=False)[0].split(","))))
    timer = {i: 0 for i in range(9)}
    for time in data:
        timer[time] += 1

    for _ in range(256):
        today = {i: 0 for i in range(9)}
        today[8] += timer[0]
        today[6] += timer[0]
        for i in range(1, 9):
            today[i - 1] += timer[i]
        timer = today

    print(sum(timer.values()))


if __name__ == "__main__":
    main()
