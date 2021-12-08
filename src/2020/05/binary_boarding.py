from pathlib import Path

from aoc.utils import load_data, profiler


@profiler
def main():
    data = load_data(2020, 5, test=False)
    seat_max = 0
    seat_min = 1023
    seats = set()
    for line in data:
        line = line.translate(str.maketrans("BFRL", "1010"))
        row = int(line[:7], 2)
        column = int(line[7:], 2)
        s = row * 8 + column
        seats.add(s)
        seat_max = max(s, seat_max)
        seat_min = min(s, seat_min)
    print("Highest ID: ", seat_max)
    total = {i for i in range(seat_min, seat_max + 1)}
    print(total.difference(seats))


if __name__ == "__main__":
    main()
