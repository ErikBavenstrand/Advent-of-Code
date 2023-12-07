# Advent of Code 2023 Day 07
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/7


def evaluate_hand(hand: str) -> tuple[int, int]:
    """Get the value of a camel poker hand.

    Args:
        hand: A poker hand.

    Returns:
        The value of the hand.
    """
    card_values = {
        "A": "14",
        "K": "13",
        "Q": "12",
        "J": "11",
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
    unique_cards_count = len(set(hand))
    counts = [hand.count(card) for card in set(hand)]
    tie_break_value = int("".join(card_values[card] for card in hand))

    # Five of a kind
    if unique_cards_count == 1 and 5 in counts:
        return 7, tie_break_value

    # Four of a kind
    if unique_cards_count == 2 and 4 in counts:
        return 6, tie_break_value

    # Full house
    if unique_cards_count == 2 and 3 in counts and 2 in counts:
        return 5, tie_break_value

    # Three of a kind
    if unique_cards_count == 3 and 3 in counts:
        return 4, tie_break_value

    # Two pairs
    if unique_cards_count == 3 and counts.count(2) == 2:
        return 3, tie_break_value

    # One pair
    if unique_cards_count == 4 and 2 in counts:
        return 2, tie_break_value

    # High card
    return 1, tie_break_value


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
        hand_type, hand_value = evaluate_hand(hand)
        hand_values.append((hand, bid, hand_type, hand_value))
    hand_values.sort(key=lambda x: (x[2], x[3]))
    return sum(int(bid) * (i + 1) for i, (_, bid, _, _) in enumerate(hand_values))


def evaluate_hand_part_b(hand: str) -> tuple[int, int]:
    """Get the value of a camel poker hand.

    Args:
        hand: A poker hand.

    Returns:
        The value of the hand.
    """
    card_values = {
        "A": "14",
        "K": "13",
        "Q": "12",
        "T": "11",
        "9": "10",
        "8": "09",
        "7": "08",
        "6": "07",
        "5": "06",
        "4": "05",
        "3": "04",
        "2": "03",
        "J": "02",
    }
    unique_cards_count = len(set(hand))
    counts = [hand.count(card) for card in set(hand)]
    tie_break_value = int("".join(card_values[card] for card in hand))

    # Five of a kind
    if (unique_cards_count == 1 and 5 in counts) or ():
        return 7, tie_break_value

    # Four of a kind
    if unique_cards_count == 2 and 4 in counts:
        return 6, tie_break_value

    # Full house
    if unique_cards_count == 2 and 3 in counts and 2 in counts:
        return 5, tie_break_value

    # Three of a kind
    if unique_cards_count == 3 and 3 in counts:
        return 4, tie_break_value

    # Two pairs
    if unique_cards_count == 3 and counts.count(2) == 2:
        return 3, tie_break_value

    # One pair
    if unique_cards_count == 4 and 2 in counts:
        return 2, tie_break_value

    # High card
    return 1, tie_break_value


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    return None
