from collections import Counter, deque

from aoc.utils import load_data, profiler


def decode(line: list[frozenset]):
    len2num = {2: 1, 4: 4, 3: 7, 7: 8}
    encodings: dict[int, frozenset] = {x: frozenset() for x in range(10)}
    queue = deque()
    for pattern in line:
        if (i := len(pattern)) in len2num:
            encodings[len2num[i]] = pattern
        else:
            queue.append(pattern)

    while queue:
        e = encodings.copy()
        pattern: frozenset = queue.popleft()
        l = len(pattern)
        if l == 6:
            if encodings[4].issubset(pattern):
                encodings[9] = pattern
            elif not encodings[1].issubset(pattern):
                encodings[6] = pattern
            elif len(pattern - encodings[5]) == 2:
                encodings[0] = pattern

        elif l == 5:
            if encodings[1].issubset(pattern):
                encodings[3] = pattern
            elif pattern.issubset(encodings[6]):
                encodings[5] = pattern
            elif len(pattern - encodings[4]) == 3:
                encodings[2] = pattern
        if e == encodings:
            queue.append(pattern)
    decodings = {v: k for k, v in encodings.items()}
    return decodings


def translate(decodings: dict[frozenset, int], output: list[frozenset]) -> int:
    n = 3
    num = 0
    for code in output:
        num += decodings[code] * 10 ** n
        n -= 1
    return num


@profiler
def part1(outputs: list[frozenset]) -> int:
    c = Counter()
    for line in outputs:
        c.update([len(pattern) for pattern in line])
    return sum([c[2], c[4], c[3], c[7]])


@profiler
def part2(data) -> int:
    return sum([translate(decode(signal), output) for signal, output in data])


def main():
    data = load_data(test=False)
    signals, outputs = [], []
    for line in data:
        i, o = line.split(" | ")
        signals.append(list(map(frozenset, i.split())))
        outputs.append(list(map(frozenset, o.split())))
    print(part1(outputs))
    data = zip(signals, outputs)
    print(part2(data))


if __name__ == "__main__":
    main()
