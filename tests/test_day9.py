from advent_of_code_2023.day9 import extrapolate, extrapolate_backwords

test_data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def test_extrapolate_report() -> None:
    result = 0
    for line in test_data.splitlines():
        arr = [int(x.strip()) for x in line.split()]
        result += extrapolate(arr)
    assert result == 114


def test_extrapolate_backwards() -> None:
    result = 0
    for line in test_data.splitlines():
        arr = [int(x.strip()) for x in line.split()]
        result += extrapolate_backwords(arr)
    assert result == 2
