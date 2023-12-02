from collections import defaultdict

from .day1 import decode_calibration_value_part_1, decode_calibration_value_part_2
from .day2 import get_power_set, is_game_possible, process_game_data


def day1_part1(file_name: str = "data/day1.txt") -> None:
    result = 0
    with open(file_name, "r") as file:
        for line in file:
            result += decode_calibration_value_part_1(line.strip())
    print("Result for day1 part1: ", result)


def day1_part2(file_name: str = "data/day1.txt") -> None:
    result = 0
    with open(file_name, "r") as file:
        for line in file:
            result += decode_calibration_value_part_2(line.strip())
    print("Result for day1 part2: ", result)


def day2_part1(file_name: str = "data/day2.txt") -> None:
    result = 0
    available_cube = defaultdict(int, {"red": 12, "green": 13, "blue": 14})

    with open(file_name, "r") as file:
        for line in file:
            game_data = process_game_data(line.strip())
            if is_game_possible(game_data[1], available_cube):
                result += game_data[0]
    print("Result for day2 part1: ", result)


def day2_part2(file_name: str = "data/day2.txt") -> None:
    result = 0

    with open(file_name, "r") as file:
        for line in file:
            game_data = process_game_data(line.strip())
            result += get_power_set(game_data[1])
    print("Result for day2 part2: ", result)
