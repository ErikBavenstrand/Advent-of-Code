# Advent of Code 2021 Day 10
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/10

import collections


def part_a(data: list[str]):
    pairs = {")": "(", "}": "{", "]": "[", ">": "<"}
    scores = {")": 3, "}": 1197, "]": 57, ">": 25137}

    complete_lines = []
    sum = 0
    for line in data:
        q = collections.deque()
        complete_lines.append(line)
        for char in line:
            if char == "(" or char == "{" or char == "[" or char == "<":
                q.append(char)
            elif char == ")" or char == "}" or char == "]" or char == ">":
                p = q.pop()
                if pairs[char] != p:
                    sum += scores[char]
                    complete_lines.pop()
                    break

    return sum


def part_b(data: list[str]):
    pairs = {")": "(", "}": "{", "]": "[", ">": "<"}
    scores = {")": 3, "}": 1197, "]": 57, ">": 25137}

    complete_lines = []
    sum = 0
    for line in data:
        q = collections.deque()
        complete_lines.append(line)
        for char in line:
            if char == "(" or char == "{" or char == "[" or char == "<":
                q.append(char)
            elif char == ")" or char == "}" or char == "]" or char == ">":
                p = q.pop()
                if pairs[char] != p:
                    sum += scores[char]
                    complete_lines.pop()
                    break

    pairs = {"(": ")", "{": "}", "[": "]", "<": ">"}
    scores = {")": 1, "}": 3, "]": 2, ">": 4}

    sums = [0] * len(complete_lines)
    for i, line in enumerate(complete_lines):
        q = collections.deque()
        for char in line:
            if char == "(" or char == "{" or char == "[" or char == "<":
                q.append(char)
            elif char == ")" or char == "}" or char == "]" or char == ">":
                p = q.pop()
        missing = list(map(lambda item: pairs[item], list(q)))
        missing.reverse()

        for char in missing:
            sums[i] = (sums[i] * 5) + scores[char]

    return sorted(sums)[int((len(sums)) / 2)]
