from .day1 import decode_calibration_value_part_1, decode_calibration_value_part_2


def day1_part1(file_name: str = "data/day1.txt") -> None:
    result = 0
    with open(file_name, "r") as file:
        for line in file:
            result += decode_calibration_value_part_1(line.strip())
    print("Result for day1 puzzel: ", result)


def day1_part2(file_name: str = "data/day1.txt") -> None:
    result = 0
    with open(file_name, "r") as file:
        for line in file:
            result += decode_calibration_value_part_2(line.strip())
    print("Result for day1 puzzel: ", result)
