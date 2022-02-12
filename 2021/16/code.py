# Advent of Code 2021 Day 16
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/16

import math


def pop(tr, n):
    ret = tr[0][:n]
    tr[0] = tr[0][n:]
    return ret


def decode(tr):
    version = int(pop(tr, 3), 2)
    type_id = int(pop(tr, 3), 2)
    global version_sum
    version_sum += version

    match type_id:
        case 4:
            return decode_literal(tr)
        case _:
            return decode_operator(tr, type_id)


def decode_literal(tr):
    num = []
    while True:
        ind, *val = pop(tr, 5)
        num += val
        if ind == "0":
            break
    return int("".join(num), 2)


def decode_operator(tr, type_id):
    length_type_id = int(pop(tr, 1))

    sbp_values = []
    match length_type_id:
        case 0:
            len_sbp = int(pop(tr, 15), 2)
            sbp = [pop(tr, len_sbp)]
            while sbp[0]:
                sbp_values.append(decode(sbp))
        case 1:
            num_sbp = int(pop(tr, 11), 2)
            sbp_values = [decode(tr) for _ in range(num_sbp)]

    match type_id:
        case 0:
            return sum(sbp_values)
        case 1:
            return math.prod(sbp_values)
        case 2:
            return min(sbp_values)
        case 3:
            return max(sbp_values)
        case 5:
            return sbp_values[0] > sbp_values[1]
        case 6:
            return sbp_values[0] < sbp_values[1]
        case 7:
            return sbp_values[0] == sbp_values[1]

    return None


version_sum = 0


def part_a(data: list[str]):
    tr = data.copy()
    value = int(tr[0], 16)
    tr[0] = format(value, f'0>{len(tr[0]) * 4}b')
    decode(tr)

    return version_sum


def part_b(data: list[str]):
    tr = data.copy()
    value = int(tr[0], 16)
    tr[0] = format(value, f'0>{len(tr[0]) * 4}b')
    value = decode(tr)

    return value
