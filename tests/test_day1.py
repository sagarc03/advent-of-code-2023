import pytest

from advent_of_code_2023.day1 import (
    decode_calibration_value_part_1,
    decode_calibration_value_part_2,
)


@pytest.mark.parametrize(
    "decode_string,decode_value",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ],
)
def test_calibration_value_decoder(decode_string: str, decode_value: str) -> None:
    assert decode_calibration_value_part_1(decode_string) == decode_value


@pytest.mark.parametrize(
    "decode_string,decode_value",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_calibration_value_decoder2(decode_string: str, decode_value: str) -> None:
    assert decode_calibration_value_part_2(decode_string) == decode_value
