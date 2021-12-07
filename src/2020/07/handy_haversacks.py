from pathlib import Path
from collections import deque
import re
from time import perf_counter
search = "shiny gold"
parent = re.compile(r"(\w+ \w+) bags contain")
children = re.compile(r"(\d+) (\w+ \w+) bags?")


def main(filename: str):
    with open(Path(__file__).absolute().parent / filename) as f:
        data = [line.strip() for line in f.readlines()]
    bags = {}
    for line in data:
        bag = parent.match(line).group(1)
        items = {match.group(2): int(match.group(1))
                 for match in children.finditer(line)}
        bags[bag] = items
    tmp = bags.copy()

    # Part 1 verbose but more efficient
    to_remove = set()
    containers = set()
    match = False
    while True:
        for bag in bags:
            if search in bags[bag]:
                containers.add(bag)
                match = True
            for b in bags[bag]:
                if b in containers and bag not in containers:
                    containers.add(bag)
                    match = True
            if match:
                match = False
                to_remove.add(bag)
        if to_remove:
            for b in to_remove:
                bags.pop(b)
            to_remove.clear()
        else:
            break
    print(len(containers))

    # Part 2
    bags = tmp.copy()
    cache = {}

    def count(color):
        if color not in cache:
            cache[color] = sum(c * (1+count(name))
                               for name, c in bags[color].items())
        return cache[color]
    print(count(search))


if __name__ == "__main__":
    for filename in ["test.txt", "input.txt"]:
        main(filename)
