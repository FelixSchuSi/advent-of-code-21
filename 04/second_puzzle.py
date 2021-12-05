from typing import List, Tuple

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()


def parse_input(lines: List[str]) -> Tuple[List[int], List[List[List[int]]]]:
    numbers_to_draw = list(map(int, lines[0].strip().split(",")))

    board_lines: List[str] = lines[1:]
    boards: List[List[List[int]]] = []
    current_board: List[List[int]] = []
    for line in board_lines:
        if line == "\n":
            if len(current_board) > 0:
                boards.append(current_board)
            current_board = []
            continue
        line = line.strip()
        chars: List[str] = list(filter(lambda x: x != "", line.split(" ")))

        current_board.append(list(map(int, chars)))

    return (numbers_to_draw, boards)


def did_board_win(board: List[List[int]]) -> bool:
    index_of_possible_column_wins = list(range(len(board[0])))

    for row in board:
        drawn_numbers = list(filter(lambda x: x == -1, row))
        if len(drawn_numbers) == len(row):
            print("win by row")
            return True

        for index, cell in enumerate(row):
            if cell != -1:
                index_of_possible_column_wins = list(
                    filter(lambda x: x != index, index_of_possible_column_wins)
                )

    if len(index_of_possible_column_wins) > 0:
        print("win by column")
        return True

    return False


def draw_number(number: int, initial_boards: List[List[List[int]]]):
    boards = initial_boards
    for board in boards:
        for row_index, row in enumerate(board):
            for col_index, cell in enumerate(row):
                if cell == number:
                    board[row_index][col_index] = -1
    return boards


def calc_score(board: List[List[int]], number):
    board_score = 0
    for row in board:
        for cell in row:
            if cell != -1:
                board_score += cell

    return board_score * number


numbers_to_draw, boards = parse_input(lines)

for number in numbers_to_draw:
    print(f"drawing number: {number}")
    boards = draw_number(number, boards)

    for index, board in enumerate(boards):
        if did_board_win(board):
            score = calc_score(board, number)
            print(f"board no. {index} won with score {score} \n {board}")
            boards = list(filter(lambda x: board is not x, boards))
            if len(boards) == 0:
                exit()
