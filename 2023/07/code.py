# Advent of Code 2023 Day 07
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/7


def get_tie_break_value(hand: str, joker: bool = False) -> int:
    """Get the tie break value of a camel poker hand.

    Args:
        hand: A poker hand.
        joker: Whether to treat Jacks as Jokers.

    Returns:
        The tie break value of the hand.
    """
    card_values = {
        "A": "14",
        "K": "13",
        "Q": "12",
        "J": "01" if joker else "11",
        "T": "10",
        "9": "09",
        "8": "08",
        "7": "07",
        "6": "06",
        "5": "05",
        "4": "04",
        "3": "03",
        "2": "02",
    }
    return int("".join(card_values[card] for card in hand))


def evaluate_hand(hand: str) -> int:
    """Get the value of a camel poker hand.

    Args:
        hand: A poker hand.

    Returns:
        The value of the hand.
    """

    unique_cards_count = len(set(hand))
    counts = [hand.count(card) for card in set(hand)]

    # Five of a kind
    if unique_cards_count == 1 and 5 in counts:
        return 7

    # Four of a kind
    if unique_cards_count == 2 and 4 in counts:
        return 6

    # Full house
    if unique_cards_count == 2 and 3 in counts and 2 in counts:
        return 5

    # Three of a kind
    if unique_cards_count == 3 and 3 in counts:
        return 4

    # Two pairs
    if unique_cards_count == 3 and counts.count(2) == 2:
        return 3

    # One pair
    if unique_cards_count == 4 and 2 in counts:
        return 2

    # High card
    return 1


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    hand_values: list[tuple[str, str, int, int]] = []
    for line in data:
        hand, bid = line.split()
        tie_break_value = get_tie_break_value(hand)
        hand_value = evaluate_hand(hand)
        hand_values.append((hand, bid, hand_value, tie_break_value))
    hand_values.sort(key=lambda x: (x[2], x[3]))
    return sum(i * int(bid) for i, (_, bid, _, _) in enumerate(hand_values, start=1))


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    hand_values: list[tuple[str, str, int, int]] = []
    for line in data:
        hand, bid = line.split()
        tie_break_value = get_tie_break_value(hand, joker=True)
        hand_value = max(
            evaluate_hand(hand.replace("J", card)) for card in "J23456789TQKA"
        )
        hand_values.append((hand, bid, hand_value, tie_break_value))
    hand_values.sort(key=lambda x: (x[2], x[3]))
    return sum(int(bid) * i for i, (_, bid, _, _) in enumerate(hand_values, start=1))
