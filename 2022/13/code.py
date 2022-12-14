# Advent of Code 2022 Day 13
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/13
from __future__ import annotations

import functools
from typing import Literal, Union

SignalType = Union[int, list["SignalType"]]


class Packet:
    """Packet."""

    def __init__(self, packet: Union[str, list[SignalType]]) -> None:
        """Initialize a Packet.

        Args:
            packet: Either string och list representation of packet.

        Raises:
            NotImplementedError: If anything other than string or list is sent.
        """
        if isinstance(packet, str):
            self.packet: list[SignalType] = eval(packet)
        elif isinstance(packet, list):
            self.packet: list[SignalType] = packet
        else:
            raise NotImplementedError

    def __repr__(self) -> str:
        """String representation of Packet.

        Returns:
            Representation of Packet.
        """
        return str(self.packet)

    def __lt__(self, signal: Packet) -> bool:
        """Less than override.

        Args:
            signal: Compared signal.

        Returns:
            True if self is less than signal.
        """
        if Packet.__compare(self.packet, signal.packet) is True:
            return True
        return False

    def __le__(self, signal: Packet) -> bool:
        """Less than equal override.

        Args:
            signal: Compared signal.

        Returns:
            True if self is less than equal signal.
        """
        if Packet.__compare(self.packet, signal.packet) is not False:
            return True
        return False

    def __gt__(self, signal: Packet) -> bool:
        """Greater than override.

        Args:
            signal: Compared signal.

        Returns:
            True if self is greater than signal.
        """
        if Packet.__compare(self.packet, signal.packet) is False:
            return True
        return False

    def __ge__(self, signal: Packet) -> bool:
        """Greater than equal override.

        Args:
            signal: Compared signal.

        Returns:
            True if self is greater than equal signal.
        """
        if Packet.__compare(self.packet, signal.packet) is not True:
            return True
        return False

    def __eq__(self, signal: Packet) -> bool:
        """Equal override.

        Args:
            signal: Compared signal.

        Returns:
            True if self is equal signal.
        """
        if Packet.__compare(self.packet, signal.packet) is None:
            return True
        return False

    def __ne__(self, signal: Packet) -> bool:
        """Not equal override.

        Args:
            signal: Compared signal.

        Returns:
            True if self is not equal signal.
        """
        if Packet.__compare(self.packet, signal.packet) is not None:
            return True
        return False

    @staticmethod
    def __compare(
        left_signal: list[SignalType], right_signal: list[SignalType]
    ) -> Union[bool, None]:
        n_left, n_right = len(left_signal), len(right_signal)
        for i in range(max(n_left, n_right)):
            if i >= n_left:
                return True
            if i >= n_right:
                return False

            item_left, item_right = left_signal[i], right_signal[i]
            if isinstance(item_left, int) and isinstance(item_right, int):
                if item_left != item_right:
                    return item_left < item_right
            else:
                item_left = [item_left] if isinstance(item_left, int) else item_left
                item_right = [item_right] if isinstance(item_right, int) else item_right
                res = Packet.__compare(item_left, item_right)
                if res is not None:
                    return res


def compare_packets(left_packet: Packet, right_packet: Packet) -> Literal[-1, 1, 0]:
    """Compare function for two packets used to sort.

    Args:
        left_packet: Packet 1.
        right_packet: Packet 2.

    Returns:
        Order of packets.
    """
    if left_packet < right_packet:
        return -1
    elif left_packet > right_packet:
        return 1
    else:
        return 0


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    correct_pair_idx_sum = 0
    for i, pairs in enumerate("\n".join(data).split("\n\n")):
        left_str, right_str = pairs.splitlines()
        left, right = Packet(left_str), Packet(right_str)
        if left < right:
            correct_pair_idx_sum += i + 1
    return correct_pair_idx_sum


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    divider_packets = [Packet([[2]]), Packet([[6]])]
    packet_signals = [
        Packet(packet_str) for packet_str in " ".join(data).split()
    ] + divider_packets
    prod_divider_idx = 1
    for i, packet in enumerate(
        sorted(packet_signals, key=functools.cmp_to_key(compare_packets))
    ):
        if packet in divider_packets:
            prod_divider_idx *= i + 1
    return prod_divider_idx
