from typing import NamedTuple

from aoc.utils import load_data, profiler


class Instruction(NamedTuple):
    opcode: str
    value: int


Code = dict[int, Instruction]
Ran = dict[int, int]


def execute(instruction: Instruction) -> tuple[int, int]:
    step, acc = 1, 0
    if instruction.opcode == "acc":
        acc = instruction.value
    elif instruction.opcode == "jmp":
        step = instruction.value
    return acc, step


def run(code: Code, ran: Ran, index: int, acc: int) -> tuple[int, Ran, int]:
    while index not in ran and index in code:
        ran[index] = acc
        acc_inc, step = execute(code[index])
        acc += acc_inc
        index += step
    return acc, ran, index


@profiler
def part1(code: Code):
    acc = run(code, {}, 0, 0)[0]
    return acc


@profiler
def part2(code: Code):
    acc, ran, _ = run(code, {}, 0, 0)
    for line in list(ran.keys())[::-1]:
        if (
            code[line].opcode == "nop" and (index := line + code[line].value) not in ran
        ) or (code[line].opcode == "jmp" and (index := line + 1) not in ran):
            acc, ran, index = run(code, ran, index, ran[line])
            if index >= len(code):
                return acc


def main():
    code: Code = {}
    for index, line in enumerate(load_data(test=False)):
        a, b = line.split()
        code[index] = Instruction(a, int(b))
    print(part1(code))
    print(part2(code))


if __name__ == "__main__":
    main()
