from aoc.utils import load_data, profiler
from typing import NamedTuple
from dataclasses import dataclass


class Instruction(NamedTuple):
    code: str
    num: int
    index: int


def run(instruction: Instruction) -> tuple[int, int]:
    # print(instruction.code, instruction.num)
    step, acc = 1, 0
    if instruction.code == "nop":
        pass
    elif instruction.code == "acc":
        acc = instruction.num
    elif instruction.code == "jmp":
        step = instruction.num
    return step, acc


@profiler
def part1(instructions: dict[int, Instruction]) -> int:
    i, acc = 0, 0
    ran = set()
    while True:
        if i in ran:
            break
        else:
            ran.add(i)
            index, inc = run(instructions[i])
            i += index
            acc += inc
    return acc


@profiler
def part2(instructions: dict[int, Instruction]) -> int:
    to_change = [ins.index for ins in instructions.values()
                 if ins.code == "jmp"]
    ran = []
    causes_loop = set()
    for ins in to_change:
        i, acc = 0, 0
        ran.clear()
        tmp = instructions.copy()
        tmp[ins] = Instruction("nop", 0, ins)
        valid = True
        while True:
            if i in ran:
                causes_loop.append(ran.pop())
                valid = False
                break
            else:
                ran.add(i)
                index, inc = run(tmp[i])
                i += index
                acc += inc
                if i not in range(len(tmp)):
                    break
        if valid:
            return acc


def main():
    instructions = {}
    for index, line in enumerate(load_data(2020, 8, test=False)):
        a, b = line.split()
        instructions[index] = Instruction(a, int(b), index)
    print(part1(instructions))
    print(part2(instructions))
    test()


if __name__ == "__main__":
    main()
