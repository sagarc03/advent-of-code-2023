from collections import defaultdict

import pytest

from advent_of_code_2023.day2 import get_power_set, is_game_possible, process_game_data


@pytest.mark.parametrize(
    "input_data,output",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            (
                1,
                [
                    {"blue": 3, "red": 4},
                    {"red": 1, "green": 2, "blue": 6},
                    {"green": 2},
                ],
            ),
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            (
                2,
                [
                    {"blue": 1, "green": 2},
                    {"green": 3, "blue": 4, "red": 1},
                    {"green": 1, "blue": 1},
                ],
            ),
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            (
                3,
                [
                    {"green": 8, "blue": 6, "red": 20},
                    {"blue": 5, "red": 4, "green": 13},
                    {"green": 5, "red": 1},
                ],
            ),
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            (
                4,
                [
                    {"green": 1, "red": 3, "blue": 6},
                    {"green": 3, "red": 6},
                    {"green": 3, "blue": 15, "red": 14},
                ],
            ),
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            (
                5,
                [
                    {"red": 6, "blue": 1, "green": 3},
                    {"blue": 2, "red": 1, "green": 2},
                ],
            ),
        ),
    ],
)
def test_process_game_data(
    input_data: str, output: tuple[int, list[dict[str, int]]]
) -> None:
    assert process_game_data(input_data) == output


@pytest.mark.parametrize(
    "game_data,is_possible",
    [
        (
            [
                {"blue": 3, "red": 4},
                {"red": 1, "green": 2, "blue": 6},
                {"green": 2},
            ],
            True,
        ),
        (
            [
                {"blue": 1, "green": 2},
                {"green": 3, "blue": 4, "red": 1},
                {"green": 1, "blue": 1},
            ],
            True,
        ),
        (
            [
                {"green": 8, "blue": 6, "red": 20},
                {"blue": 5, "red": 4, "green": 13},
                {"green": 5, "red": 1},
            ],
            False,
        ),
        (
            [
                {"green": 1, "red": 3, "blue": 6},
                {"green": 3, "red": 6},
                {"green": 3, "blue": 15, "red": 14},
            ],
            False,
        ),
        (
            [
                {"red": 6, "blue": 1, "green": 3},
                {"blue": 2, "red": 1, "green": 2},
            ],
            True,
        ),
    ],
)
def test_is_game_possible(game_data: list[dict[str, int]], is_possible: bool) -> None:
    available_cubes = defaultdict(int)
    available_cubes["red"] = 12
    available_cubes["green"] = 13
    available_cubes["blue"] = 14
    assert is_game_possible(game_data, available_cubes) == is_possible


@pytest.mark.parametrize(
    "game_data,power_set",
    [
        (
            [
                {"blue": 3, "red": 4},
                {"red": 1, "green": 2, "blue": 6},
                {"green": 2},
            ],
            48,
        ),
        (
            [
                {"blue": 1, "green": 2},
                {"green": 3, "blue": 4, "red": 1},
                {"green": 1, "blue": 1},
            ],
            12,
        ),
        (
            [
                {"green": 8, "blue": 6, "red": 20},
                {"blue": 5, "red": 4, "green": 13},
                {"green": 5, "red": 1},
            ],
            1560,
        ),
        (
            [
                {"green": 1, "red": 3, "blue": 6},
                {"green": 3, "red": 6},
                {"green": 3, "blue": 15, "red": 14},
            ],
            630,
        ),
        (
            [
                {"red": 6, "blue": 1, "green": 3},
                {"blue": 2, "red": 1, "green": 2},
            ],
            36,
        ),
    ],
)
def test_power_set(game_data: list[dict[str, int]], power_set: int) -> None:
    assert get_power_set(game_data) == power_set
