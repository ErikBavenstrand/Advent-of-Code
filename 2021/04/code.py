# Advent of Code 2021 Day 04
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/4

import numpy as np


class Bingo:
    def __init__(self) -> None:
        self.board = np.empty((5, 5), dtype=np.int32)
        self.found = np.full((5, 5), 1, dtype=np.int32)
        self.added_rows = 0
        self.already_won = False

    def insert_row(self, row: str):
        self.board[self.added_rows] = np.array(row.strip("\n").split(),
                                               dtype=np.int32)
        self.added_rows += 1

    def cross_number(self, num: str):
        indices = np.asarray(np.where(self.board == int(num))).T
        for idx in indices:
            self.found[idx[0], idx[1]] = 0

    def check_bingo(self) -> bool:
        if (
            0 in np.sum(self.found, axis=0).tolist()
            or 0 in np.sum(self.found, axis=1).tolist()
        ):
            return True
        return False

    def get_score(self, mod: str):
        not_found_score = np.sum(np.multiply(self.board, self.found))
        return not_found_score * int(mod)

    def __str__(self) -> str:
        board = ""
        for i in range(5):
            for j in range(5):
                if self.found[i, j] == 0:
                    board += f"\033[92m{self.board[i, j]}\033[0m "
                else:
                    board += f"{self.board[i, j]} "
            board += "\n"
        return board


def part_a(data: list[str]):
    numbers = data[0].split(",")
    boards = []

    for inp in data[1:]:
        if inp == "":
            boards.append(Bingo())
        else:
            boards[-1].insert_row(inp)

    bingo = False
    score = 0
    for num in numbers:
        if not bingo:
            for board in boards:
                board.cross_number(num)
                if board.check_bingo():
                    bingo = True
                    score = board.get_score(num)

    return score


def part_b(data: list[str]):
    numbers = data[0].split(",")
    boards = []
    for inp in data[1:]:
        if inp == "":
            boards.append(Bingo())
        else:
            boards[-1].insert_row(inp)

    score = 0
    total_boards = len(boards)
    for num in numbers:
        for board in boards:
            if not board.already_won:
                board.cross_number(num)
                if board.check_bingo():
                    board.already_won = True
                    if total_boards == 1:
                        score = board.get_score(num)
                    total_boards -= 1

    return score
