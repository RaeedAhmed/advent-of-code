from pathlib import Path
import re
from collections import deque

search = "shiny gold"
parent = re.compile(r"(\w+ \w+) bags contain")
children = re.compile(r"(\d+) (\w+ \w+) bags?")


def main(filename: str):
    with open(Path(__file__).absolute().parent / filename) as f:
        data = [line.strip() for line in f.readlines()]
    bags = {}
    for line in data:
        bag = parent.match(line).group(1)
        items = [(int(match.group(1)), match.group(2))
                 for match in children.finditer(line)]
        bags[bag] = items
    queue = deque(bags[search])
    total = 0
    while queue:
        count, item = queue.popleft()
        total += count
        queue.extend((count * child_count, child)
                     for child_count, child in bags[item])
    print(total)


if __name__ == "__main__":
    for filename in ["test.txt", "input.txt"]:
        main(filename)
