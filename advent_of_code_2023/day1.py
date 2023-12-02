from typing import Iterator, Sequence


def decode_calibration_value_part_1(word: str) -> int:
    digits = [int(x) for x in word if x.isdigit()]
    return digits[0] * 10 + digits[-1]


spelled_out_number = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_first_digit(word: str, rng: Iterator[int] | Sequence[int]) -> int:
    for i in rng:
        for key, value in spelled_out_number.items():
            if word[i : i + len(key)] == key:
                return value
    return 0


def decode_calibration_value_part_2(word: str) -> int:
    n = len(word)
    return get_first_digit(word, range(n)) * 10 + get_first_digit(
        word, reversed(range(n))
    )
