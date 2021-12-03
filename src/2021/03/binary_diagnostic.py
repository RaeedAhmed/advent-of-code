from pathlib import Path


def part1(data: list[str], bitlength: int) -> int:
    count = {str(i): 0 for i in range(bitlength)}
    for string in data:
        for index, digit in enumerate(string):
            count[str(index)] += int(digit)
    gamma_rate, epsilon_rate = "", ""
    for i in range(bitlength):
        if count[str(i)] >= len(data)-count[str(i)]:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2(data: list[str], bitlength: int) -> int:
    def sieve(data, flip: bool) -> int:
        for i in range(bitlength):
            count = sum((int(string[i]) for string in data))
            bit = str(abs(int(count >= len(data) - count) - flip))
            data = [string for string in data if string[i] == bit]
            if len(data) == 1:
                break
        return int(data[0], 2)
    return sieve(data, 0) * sieve(data, 1)


def load_data(filename: str) -> list[str]:
    with open(Path(__file__).absolute().parent / filename) as f:
        data = [depth.strip() for depth in f.readlines()]
    return data


def run():
    data = load_data("input.txt")
    print(part1(data, 12))
    print(part2(data, 12))


if __name__ == "__main__":
    run()
