from collections import Counter


def get_strength(hand: str) -> tuple[int, str]:
    hand = hand.replace("T", chr(ord("9") + 1))
    hand = hand.replace("Q", chr(ord("9") + 3))
    hand = hand.replace("K", chr(ord("9") + 4))
    hand = hand.replace("A", chr(ord("9") + 5))
    c = Counter(hand)
    sorted_count = sorted(c.values())

    if sorted_count == [5]:
        return (10, hand)

    if sorted_count == [1, 4]:
        return (9, hand)

    if sorted_count == [2, 3]:
        return (8, hand)

    if sorted_count == [1, 1, 3]:
        return (7, hand)

    if sorted_count == [1, 2, 2]:
        return (6, hand)

    if sorted_count == [1, 1, 1, 2]:
        return (5, hand)

    return (4, hand)


def get_strength_with_joker(hand: str) -> tuple[int, str]:
    hand = hand.replace("T", chr(ord("9") + 1))
    hand = hand.replace("Q", chr(ord("9") + 2))
    hand = hand.replace("K", chr(ord("9") + 3))
    hand = hand.replace("A", chr(ord("9") + 4))
    hand = hand.replace("J", chr(ord("1") - 1))
    c = Counter(hand)
    max_other_than_J = 0
    for k, v in c.items():
        if k != "0":
            max_other_than_J = max(max_other_than_J, v)

    c = Counter(hand)
    if "0" in c:
        for k, v in c.items():
            if k != "0" and v == max_other_than_J:
                c[k] += c["0"]
                c.pop("0")
                break

    sorted_count = sorted(c.values())
    if sorted_count == [5]:
        return (10, hand)

    if sorted_count == [1, 4]:
        return (9, hand)

    if sorted_count == [2, 3]:
        return (8, hand)

    if sorted_count == [1, 1, 3]:
        return (7, hand)

    if sorted_count == [1, 2, 2]:
        return (6, hand)

    if sorted_count == [1, 1, 1, 2]:
        return (5, hand)

    return (4, hand)
