from pathlib import Path


def main(filename: str):
    with open(Path(__file__).absolute().parent / filename) as f:
        data = [line.strip() for line in f.readlines()]
    seat_max = 0
    seat_min = 1023
    seats = set()
    for line in data:
        line = line.translate(str.maketrans("BFRL", "1010"))
        row = int(line[:7], 2)
        column = int(line[7:], 2)
        s = row*8 + column
        seats.add(s)
        seat_max = max(s, seat_max)
        seat_min = min(s, seat_min)
    print("Highest ID: ", seat_max)
    total = {i for i in range(seat_min, seat_max + 1)}
    print(total.difference(seats))


if __name__ == "__main__":
    for filename in ["test.txt", "input.txt"]:
        main(filename)
