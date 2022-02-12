# Advent of Code 2021 Day 24
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/24

from functools import lru_cache


@lru_cache(maxsize=None)
def solve(step: int = 0, z: int = 0):
    global inst

    def default_state():
        return [0, 0, 0, 0]

    def var_to_idx(var: str):
        return ord(var) - ord("w")

    def write(state: list[int], var: str, val: int):
        state[var_to_idx(var)] = val
        return state

    def read(state: list[int], var: str):
        return state[var_to_idx(var)] if "w" <= var <= "z" else int(var)

    for input in range(1, 10):
        state = default_state()
        state = write(state, "z", z)
        state = write(state, inst[step][1], input)
        i = step + 1
        while True:
            if i == len(inst):
                return None if read(state, "z") != 0 else str(input)
            curr = inst[i]
            if curr[0] == "inp":
                solution = solve(i, read(state, "z"))
                if solution is not None:
                    return str(input) + solution
                break
            if curr[0] == "add":
                state = write(state, curr[1], read(
                    state, curr[1]) + read(state, curr[2]))
            if curr[0] == "mul":
                state = write(state, curr[1], read(
                    state, curr[1]) * read(state, curr[2]))
            if curr[0] == "div":
                state = write(state, curr[1], read(
                    state, curr[1]) // read(state, curr[2]))
            if curr[0] == "mod":
                state = write(state, curr[1], read(
                    state, curr[1]) % read(state, curr[2]))
            if curr[0] == "eql":
                state = write(state, curr[1], int(read(
                    state, curr[1]) == read(state, curr[2])))
            i += 1


# All instructions are stored in this global var
inst = []


def part_a(data: list[str]):
    global inst
    inst = [line.split() for line in data]
    print(solve())
    return None


def part_b(data: list[str]):
    return None
