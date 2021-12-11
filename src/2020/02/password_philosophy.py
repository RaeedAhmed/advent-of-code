import re
from functools import partial
from typing import NamedTuple

from aoc.utils import load_data, profiler


class Entry(NamedTuple):
    num1: int
    num2: int
    char: str
    word: str


def parse_entry(pattern: re.Pattern, entry: str) -> Entry:
    num1, num2, char, word = pattern.findall(entry)[0]
    return Entry(int(num1), int(num2), char, word)


def verify_count(entry: Entry) -> bool:
    count = sum(((letter == entry.char) for letter in entry.word))
    return entry.num1 <= count <= entry.num2


def verify_position(entry: Entry) -> bool:
    return (entry.word[entry.num1 - 1] == entry.char) ^ (
        entry.word[entry.num2 - 1] == entry.char
    )


@profiler
def main() -> None:
    data = load_data(test=False)
    pattern = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")
    parse = partial(parse_entry, pattern)
    entries = [parse(entry) for entry in data]
    part1 = sum((verify_count(entry) for entry in entries))
    part2 = sum((verify_position(entry) for entry in entries))
    print(part1, part2, sep="\n")


if __name__ == "__main__":
    main()
