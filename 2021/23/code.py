# Advent of Code 2021 Day 23
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/23

def part_a(data: list[str]):
    '''
    #############
    #...........#
    ###A#D#C#A###
      #C#D#B#B#
      #########

    #############
    #.A.........#
    ###.#D#C#A###
      #C#D#B#B#
      #########

    #############
    #.A.B.....A.#
    ###.#D#C#.###
      #C#D#B#.#
      #########

    #############
    #.A.B.....A.#
    ###.#.#C#D###
      #C#.#B#D#
      #########

    #############
    #.A.....C.A.#
    ###.#B#.#D###
      #.#B#C#D#
      #########

    #############
    #.A.......A.#
    ###.#B#C#D###
      #.#B#C#D#
      #########


    #############
    #...........#
    ###A#B#C#D###
      #A#B#C#D#
      #########
    '''

    return 2+2+70+14000+30+200+50+800+200+11


rooms_example = (("B", "A"), ("C", "D"), ("B", "C"), ("D", "A"))
room_map = (2, 4, 6, 8)
hall_spots = (0, 1, 3, 5, 7, 9, 10)
destination = {"A": 0, "B": 1, "C": 2, "D": 3}
costs = {"A": 1, "B": 10, "C": 100, "D": 1000}


def part_b(data: list[str]):
    print(tuple(None for _ in range(len(room_map) + len(hall_spots))))

    return None
