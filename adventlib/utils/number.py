from typing import Union, overload


@overload
def clamp(
    value: int, min_value: Union[int, float], max_value: Union[int, float]
) -> int:
    ...


@overload
def clamp(
    value: int, min_value: Union[int, float], max_value: Union[int, float]
) -> float:
    ...


def clamp(
    value: Union[int, float], min_value: Union[int, float], max_value: Union[int, float]
) -> Union[int, float]:
    """Clamp value to range [min_value, max_value].

    Args:
        value: Value to be clamped.
        min_value: Minimum value.
        max_value: Maximum value.

    Returns:
        Clamped value.
    """
    return max(min_value, min(max_value, value))
