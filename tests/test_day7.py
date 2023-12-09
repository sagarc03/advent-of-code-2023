from advent_of_code_2023.day7 import get_strength, get_strength_with_joker

test_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


def test_get_strength() -> None:
    hands: list[tuple[str, int]] = []
    for line in test_data.splitlines():
        hand, rank = line.split()
        hands.append((hand, int(rank)))

    result = 0

    for i, (hand, rank) in enumerate(sorted(hands, key=lambda x: get_strength(x[0]))):
        result += (i + 1) * rank

    assert result == 6440


def test_get_strength_with_joker() -> None:
    hands: list[tuple[str, int]] = []
    for line in test_data.splitlines():
        hand, rank = line.split()
        hands.append((hand, int(rank)))

    result = 0

    for i, (hand, rank) in enumerate(
        sorted(hands, key=lambda x: get_strength_with_joker(x[0]))
    ):
        result += (i + 1) * rank

    assert result == 5905
