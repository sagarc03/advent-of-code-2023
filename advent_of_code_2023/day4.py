def parse_card(card: str) -> tuple[int, set[str], set[str]]:
    card_split = card.split(":")
    card_serial_number = int(card_split[0].strip().split()[-1])
    winning_numbers, card_numbers = [
        set(x.strip().split()) for x in card_split[-1].split("|")
    ]
    return card_serial_number, winning_numbers, card_numbers


def number_cards_won(winning_numbers: set[str], card_numbers: set[str]) -> int:
    return len(winning_numbers.intersection(card_numbers))


def count_points_in_card(card: str) -> int:
    _, winning_numbers, card_numbers = parse_card(card)
    n = number_cards_won(winning_numbers, card_numbers)
    return 0 if n == 0 else 2 ** (n - 1)
