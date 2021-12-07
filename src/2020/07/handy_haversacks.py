from pathlib import Path
from collections import deque
import re

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

    def find_containers(target):
        """Part 1 recursive but inefficient"""
        containers = set()
        for bag, items in bags.items():
            if target in items:
                containers.add(bag)
                containers.update(find_containers(bag))
        return containers

    cache = {}

    def count(color):  # Part 2
        if color not in cache:
            cache[color] = sum(c * (1+count(name))
                               for name, c in bags[color].items())
        return cache[color]
    print(count(search))

    # Part 1 verbose but more efficient
    tmp = bags.copy()
    containers = set()
    match = False
    while True:
        for bag in bags:
            if search in bags[bag]:
                containers.add(bag)
                match = True
            for b in bags[bag]:
                if b in containers:
                    containers.add(bag)
                    match = True
            if match:
                match = False
                tmp.pop(bag)
        if bags == tmp:
            break
        else:
            bags = tmp.copy()
    print(len(containers))


if __name__ == "__main__":
    for filename in ["input.txt"]:
        main(filename)
