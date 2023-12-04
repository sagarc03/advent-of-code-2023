import pytest

from advent_of_code_2023.day4 import count_points_in_card, number_cards_won

test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def test_count_points_in_card() -> None:
    assert (
        sum([count_points_in_card(str(x).strip()) for x in test_data.splitlines()])
        == 13
    )


@pytest.mark.parametrize(
    "winning_numbers,card_numbers,cards_won",
    [
        ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 8, 48, 53}, 4),
        ({13, 32, 20, 16, 61}, {61, 30, 68, 82, 17, 32, 24, 19}, 2),
        ({1, 21, 53, 59, 44}, {69, 82, 63, 72, 16, 21, 14, 1}, 2),
        ({41, 92, 73, 84, 69}, {59, 84, 76, 51, 58, 5, 54, 83}, 1),
        ({87, 83, 26, 28, 32}, {88, 30, 70, 12, 93, 22, 82, 36}, 0),
        ({31, 18, 13, 56, 72}, {74, 77, 10, 23, 35, 67, 36, 11}, 0),
    ],
)
def test_number_of_cards_won(
    winning_numbers: set[str], card_numbers: set[str], cards_won: int
) -> None:  # 1, {1: 1, 2: 1, 3: 1, 3: 1, 5}
    assert number_cards_won(winning_numbers, card_numbers) == cards_won
