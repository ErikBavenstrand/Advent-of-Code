from pathlib import Path

from solution import part_a, part_b  # noqa: F401 # type: ignore

TEST_CASES_DIR = Path(__file__).parent / "test_cases"


def load_test_case(case_id: int) -> tuple[str, str, str]:
    """Load input and expected output for a test case.

    Args:
        case_id: The test case ID.

    Returns:
        A tuple containing the input data and the expected output
        for part A and part B, respectively.
    """
    input_file = TEST_CASES_DIR / f"input_{case_id}.txt"
    output_a_file = TEST_CASES_DIR / f"output_{case_id}_a.txt"
    output_b_file = TEST_CASES_DIR / f"output_{case_id}_b.txt"

    with input_file.open("r") as f:
        input_data = f.read()

    expected_a = ""
    if output_a_file.exists():
        with output_a_file.open("r") as f:
            expected_a = f.read().strip()

    expected_b = ""
    if output_b_file.exists():
        with output_b_file.open("r") as f:
            expected_b = f.read().strip()

    return input_data, expected_a, expected_b


def test_part_a_1() -> None:
    input_data, expected_a, _ = load_test_case(1)
    assert str(part_a(input_data.splitlines())) == expected_a


def test_part_b_2() -> None:
    input_data, _, expected_b = load_test_case(2)

    assert str(part_b(input_data.splitlines())) == expected_b