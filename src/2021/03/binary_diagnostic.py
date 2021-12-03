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


class Test:
    def p1():
        data = load_data("test.txt")
        count = {str(i): 0 for i in range(5)}
        for string in data:
            for index, digit in enumerate(string):
                count[str(index)] += int(digit)
        gamma_rate, epsilon_rate = "", ""
        for i in range(5):
            if count[str(i)] >= len(data)-count[str(i)]:
                gamma_rate += "1"
                epsilon_rate += "0"
            else:
                gamma_rate += "0"
                epsilon_rate += "1"
        assert(gamma_rate == "10110")
        assert(epsilon_rate == "01001")
        product = int(gamma_rate, 2) * int(epsilon_rate, 2)
        assert(product == 198)
        print("\n***Part 1 passed***\n")

    def p2():
        data = load_data("test.txt")
        bitlength = 5
        count = sum((int(string[0]) for string in data))
        assert(count == 7)

        def sieve(data, flip: bool):
            for i in range(bitlength):
                count = sum((int(string[i]) for string in data))
                bit = str(abs(int(count >= len(data) - count) - flip))
                data = [string for string in data if string[i] == bit]
                if len(data) == 1:
                    break
            return data[0]
        assert(sieve(data, 0) == '10111')
        assert(sieve(data, 1) == '01010')
        assert(int(sieve(data, 0), 2) * int(sieve(data, 1), 2) == 230)
        print("\n***Part 2 passed***\n")


def run():
    data = load_data("input.txt")
    print(part1(data, 12))
    print(part2(data, 12))


if __name__ == "__main__":
    Test.p1()
    Test.p2()
    run()
