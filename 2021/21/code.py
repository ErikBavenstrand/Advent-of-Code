# Advent of Code 2021 Day 21
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/21

from functools import lru_cache


def get_start_pos(data: list[str]):
    p1 = int(data[0].split(": ")[1])
    p2 = int(data[1].split(": ")[1])
    return (p1, p2)


def move(pos, roll):
    pos = (pos + roll) % 10
    return 10 if pos == 0 else pos


def part_a(data: list[str]):
    pos = list(get_start_pos(data))
    score = [0, 0]
    dice = 0
    dice_rolls = 0
    turn = 0
    win_score = 1000

    while score[0] < win_score and score[1] < win_score:
        roll = 0
        for _ in range(3):
            dice = (dice + 1) % 100
            dice = 100 if dice == 0 else dice
            roll += dice
        if turn == 0:
            pos[0] = move(pos[0], roll)
            score[0] += pos[0]
        else:
            pos[1] = move(pos[1], roll)
            score[1] += pos[1]
        dice_rolls += 3
        turn = turn ^ 1

    return min(score) * dice_rolls


def part_b(data: list[str]):
    pos = get_start_pos(data)

    dirac_cases = [[3, 1], [4, 3], [
        5, 6], [6, 7], [7, 6], [8, 3], [9, 1]]
    win_score = 21

    @lru_cache(maxsize=None)
    def split(pos: tuple[int, int], score: tuple[int, int], turn: int):
        p1_wins = p2_wins = 0
        for roll, universes in dirac_cases:
            (p1, p2) = pos
            (p1_score, p2_score) = score

            if turn == 0:
                p1 = move(p1, roll)
                p1_score += p1
            else:
                p2 = move(p2, roll)
                p2_score += p2

            if p1_score >= win_score:
                p1_wins += universes
            elif p2_score >= win_score:
                p2_wins += universes
            else:
                wins = split((p1, p2), (p1_score, p2_score), turn ^ 1)
                p1_wins += wins[0] * universes
                p2_wins += wins[1] * universes
        return p1_wins, p2_wins

    return max(split(pos, (0, 0), 0))
