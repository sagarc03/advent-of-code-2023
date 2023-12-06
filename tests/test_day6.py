from advent_of_code_2023.day6 import (
    number_of_ways_to_beat,
    number_of_ways_to_beat_binary_search,
)

test_data: str = """Time:      7  15   30
Distance:  9  40  200"""


def test_number_of_ways_to_beat() -> None:
    times = [int(x) for x in test_data.split("\n")[0].split(":")[1].strip().split()]
    durations = [int(x) for x in test_data.split("\n")[1].split(":")[1].strip().split()]
    result = 1
    for t, d in zip(times, durations):
        result *= number_of_ways_to_beat(t, d)
    assert result == 288


def test_number_of_ways_to_beat_start_from() -> None:
    times = int(test_data.split("\n")[0].split(":")[1].replace(" ", ""))
    durations = int(test_data.split("\n")[1].split(":")[1].replace(" ", ""))
    assert number_of_ways_to_beat(times, durations, 14) == 71503


def test_number_of_ways_to_beat_from_binary() -> None:
    times = [int(x) for x in test_data.split("\n")[0].split(":")[1].strip().split()]
    durations = [int(x) for x in test_data.split("\n")[1].split(":")[1].strip().split()]
    result = 1
    for t, d in zip(times, durations):
        res = number_of_ways_to_beat_binary_search(t, d)
        result *= res
    assert result == 288


def test_number_of_ways_to_beat_start_from_binary() -> None:
    times = int(test_data.split("\n")[0].split(":")[1].replace(" ", ""))
    durations = int(test_data.split("\n")[1].split(":")[1].replace(" ", ""))
    assert number_of_ways_to_beat_binary_search(times, durations, 14) == 71503
