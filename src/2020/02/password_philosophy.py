from pathlib import Path


class Entry:
    def __init__(self, raw: str) -> None:
        count, letter, password = raw.strip().split()
        self.count: list[int] = [int(num) for num in count.split("-")]
        self.letter: str = letter[0]
        self.password: str = password

    def verify_count(self) -> bool:
        count = 0
        for letter in self.password:
            count += (letter == self.letter)
        if self.count[0] <= count <= self.count[1]:
            return True
        return False

    def verify_position(self) -> bool:
        a, b = self.password[self.count[0]-1], self.password[self.count[1]-1]
        if (a == self.letter) ^ (b == self.letter):
            return True
        return False


def main(filename: str):
    with open(Path(__file__).absolute().parent / filename) as f:
        data = f.readlines()
    p1 = [line for line in data if Entry(line).verify_count()]
    print(f"p1: {len(p1)}")
    p2 = [line for line in data if Entry(line).verify_position()]
    print(f"p2: {len(p2)}")


if __name__ == "__main__":
    for filename in ["test.txt", "input.txt"]:
        main(filename)
