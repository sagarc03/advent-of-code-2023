from advent_of_code_2023.day3 import get_valid_gear_ratio, get_valid_numbers

test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_get_valid_numbers() -> None:
    assert sum(get_valid_numbers([str(x).strip() for x in test_data.split()])) == 4361


def test_get_valid_gear_ratio() -> None:
    assert (
        sum(get_valid_gear_ratio([str(x).strip() for x in test_data.split()])) == 467835
    )
