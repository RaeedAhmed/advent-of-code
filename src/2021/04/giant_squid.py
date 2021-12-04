from pathlib import Path


def load_data(filename: str) -> tuple[list[str], list[list[list[int]]]]:
    with open(Path(__file__).absolute().parent / filename) as f:
        data = [line.strip() for line in f.readlines()]
        draw = [num for num in data.pop(0).split(",")]
        boards = []
        for i in range(1, len(data), 6):
            boards.append([[int(num) for num in row.split()]
                          for row in data[i:i+6][:5]])
        return draw, boards


def part1(filename: str) -> int:
    draw, boards = load_data(filename)
    counter = {board: {'r': {row: 0 for row in range(
        5)}, 'c': {column: 0 for column in range(5)}} for board in range(len(boards))}

    def bingo() -> tuple[int, int]:
        for call in draw:
            for board in range(len(boards)):
                for row in range(5):
                    for column in range(5):
                        if str(boards[board][row][column]) == call:
                            counter[board]['r'][row] += 1
                            counter[board]['c'][column] += 1
                            boards[board][row][column] = False
                        if counter[board]['r'][row] == 5 or counter[board]['c'][column] == 5:
                            return int(call), board
    call, board = bingo()
    sum_board = sum([sum(row) for row in boards[board]])
    product = call * sum_board
    return product


def part2(filename: str):
    draw, boards = load_data(filename)
    counter = {board: {'r': {row: 0 for row in range(
        5)}, 'c': {column: 0 for column in range(5)}} for board in range(len(boards))}

    def bingo() -> tuple[int, int]:
        winners = []
        calls = []
        for call in draw:
            for board in range(len(boards)):
                if board in winners:
                    continue
                for row in range(5):
                    for column in range(5):
                        if str(boards[board][row][column]) == call:
                            counter[board]['r'][row] += 1
                            counter[board]['c'][column] += 1
                            boards[board][row][column] = False
                        if counter[board]['r'][row] == 5 or counter[board]['c'][column] == 5:
                            winners.append(board)
                            calls.append(int(call))
        return calls[-1], winners[-1]
    call, board = bingo()
    sum_board = sum([sum(row) for row in boards[board]])
    product = call * sum_board
    return product


def run():
    for filename in ["test.txt", "input.txt"]:
        print(filename, part1(filename), part2(filename))


if __name__ == "__main__":
    run()
