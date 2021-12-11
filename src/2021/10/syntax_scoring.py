from collections import deque

from aoc.utils import load_data, profiler


@profiler
def solution(data: deque[str]) -> tuple[int, int]:
    pair = {"(": ")", "[": "]", "{": "}", "<": ">"}
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    ipoints = {")": 1, "]": 2, "}": 3, ">": 4}
    sum, isum = 0, []
    queue = deque()
    while data:
        invalid = False
        queue.clear()
        line = data.popleft()
        for char in line:
            if char in pair:
                queue.append(pair[char])
            else:
                opening = queue.pop()
                if char != opening:
                    sum += points[char]
                    invalid = True
                    break
        if not invalid:
            s = 0
            while queue:
                s *= 5
                s += ipoints[queue.pop()]
            isum.append(s)
    middle = sorted(isum)[round(len(isum) / 2)]
    return sum, middle


def main():
    data = deque(load_data(test=False))
    print(solution(data))


if __name__ == "__main__":
    main()
