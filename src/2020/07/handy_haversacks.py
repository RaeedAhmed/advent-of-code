from pathlib import Path
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
        items = {match.group(2): int(match.group(1)) for match in children.finditer(line)}
        bags[bag] = items
    cache = {}
    def count(color):
        if color not in cache:
            cache[color] = sum(c * (1+count(name)) for name, c in bags[color].items())
        return cache[color]
    
    print(count(search))

if __name__ == "__main__":
    for filename in ["test.txt"]:
        main(filename)
