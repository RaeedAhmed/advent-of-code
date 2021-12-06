from pathlib import Path


def main(filename: str):
    with open(Path(__file__).absolute().parent / filename) as f:
        data = [int(num) for num in f.read().strip().split(",")]
    timer = {i: 0 for i in range(9)}
    for time in data:
        timer[time] += 1

    for _ in range(256):
        today = {i: 0 for i in range(9)}
        today[8] += timer[0]
        today[6] += timer[0]
        for i in range(1, 9):
            today[i-1] += timer[i]
        timer = today

    print(sum(timer.values()))


if __name__ == "__main__":
    for filename in ["test.txt", "input.txt"]:
        main(filename)
