from pathlib import Path

Draws = list[str]
Row = list[int]
Board = list[Row]


def load_data(filename: str) -> tuple[Draws, list[Board]]:
    with open(Path(__file__).absolute().parent / filename) as f:
        data = [line.strip() for line in f.readlines()]
        draw = [num for num in data.pop(0).split(",")]
        boards: list[Board] = []
        for i in range(1, len(data), 6):
            boards.append([[int(num) for num in row.split()]
                          for row in data[i:i+6][:5]])
        return draw, boards


def bingo(draws: Draws, boards: list[Board]) -> list[int]:
    counter = {board: {'r': {row: 0 for row in range(
        5)}, 'c': {column: 0 for column in range(5)}} for board in range(len(boards))}
    winners = []
    calls = []
    for call in draws:
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
                        if board not in winners:
                            winners.append(board)
                            calls.append(int(call))

    scores = []
    for index in [0, -1]:
        board, call = winners[index], calls[index]
        sum_board = sum([sum(row) for row in boards[board]])
        scores.append(call * sum_board)
    return scores


def run():
    for filename in ["test.txt", "input.txt"]:
        print(bingo(*load_data(filename)))


if __name__ == "__main__":
    run()
