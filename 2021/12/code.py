# Advent of Code 2021 Day 12
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/12

from collections import defaultdict, deque


def part_a(data: list[str]):
    graph = defaultdict(set)
    for line in data:
        node1, node2 = line.split("-")
        graph[node1].add(node2)
        graph[node2].add(node1)

    initial_state = ("start", set(['start']))
    count = 0
    q = deque([initial_state])
    while q:
        cave, visited_small = q.popleft()
        if cave == "end":
            count += 1
            continue
        for neighbor in graph[cave]:
            if neighbor not in visited_small:
                new_visited_small = set(visited_small)
                if neighbor.islower():
                    new_visited_small.add(neighbor)
                q.append((neighbor, new_visited_small))
    return count


def part_b(data: list[str]):
    graph = defaultdict(set)
    for line in data:
        node1, node2 = line.split("-")
        graph[node1].add(node2)
        graph[node2].add(node1)

    initial_state = ("start", set(['start']), None)
    count = 0
    q = deque([initial_state])
    while q:
        cave, visited_small, visited_twice = q.popleft()
        if cave == "end":
            count += 1
            continue
        for neighbor in graph[cave]:
            if neighbor not in visited_small:
                new_visited_small = set(visited_small)
                if neighbor.islower():
                    new_visited_small.add(neighbor)
                q.append((neighbor, new_visited_small, visited_twice))
            elif visited_twice is None and neighbor not in ["start", "end"]:
                q.append((neighbor, visited_small, neighbor))
    return count
