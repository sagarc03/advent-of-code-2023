from collections import defaultdict

from .day1 import decode_calibration_value_part_1, decode_calibration_value_part_2
from .day2 import get_power_set, is_game_possible, process_game_data
from .day3 import get_valid_gear_ratio, get_valid_numbers
from .day4 import count_points_in_card, number_cards_won, parse_card
from .day5 import get_maps, get_seeds, get_seeds_interval
from .day6 import number_of_ways_to_beat_binary_search


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


def day3_part1(file_name: str = "data/day3.txt") -> None:
    result = 0
    with open(file_name, "r") as file:
        result += sum(get_valid_numbers([x.strip() for x in file.readlines()]))
    print("Result for day3 part1: ", result)


def day3_part2(file_name: str = "data/day3.txt") -> None:
    result = 0
    with open(file_name, "r") as file:
        result += sum(get_valid_gear_ratio([x.strip() for x in file.readlines()]))
    print("Result for day3 part2: ", result)


def day4_part1(file_name: str = "data/day4.txt") -> None:
    result = 0
    with open(file_name, "r") as file:
        for line in file:
            result += count_points_in_card(line.strip())
    print("Result for day4 part1: ", result)


def day4_part2(file_name: str = "data/day4.txt") -> None:
    store = defaultdict(int)
    with open(file_name, "r") as file:
        for line in file:
            card, winning_numbers, card_numbers = parse_card(line.strip())
            cards_won = number_cards_won(winning_numbers, card_numbers)
            store[card] += 1
            for i in range(1, cards_won + 1):
                store[card + i] += store[card]

    print("Result for day4 part1: ", sum(store.values()))


def day5_part1(file_name: str = "data/day5.txt") -> None:
    with open(file_name, "r") as file:
        data = file.read()
        seeds = get_seeds(data.split("\n\n")[0])
        maps = get_maps(data.split("\n\n")[1:])

        result = []
        for seed in seeds:
            for map in maps:
                seed = map.apply_for_value(seed)
            result.append(seed)

    print("Result for day5 part1: ", min(result))


def day5_part2(file_name: str = "data/day5.txt") -> None:
    with open(file_name, "r") as file:
        data = file.read()
        seeds = get_seeds_interval(data.split("\n\n")[0])
        maps = get_maps(data.split("\n\n")[1:])

        result = []
        for seed in seeds:
            temp = [seed]
            for map in maps:
                temp = map.apply_for_ranges(temp)
            result.append(min(temp)[0])

    print("Result for day5 part2: ", min(result))


def day6_part1(file_name: str = "data/day6.txt") -> None:
    with open(file_name, "r") as file:
        times = [int(x) for x in file.readline().split(":")[1].strip().split()]
        durations = [int(x) for x in file.readline().split(":")[1].strip().split()]

    result = 1
    for t, d in zip(times, durations):
        result *= number_of_ways_to_beat_binary_search(t, d)
    print("Result for day6 part1: ", result)


def day6_part2(file_name: str = "data/day6.txt") -> None:
    with open(file_name, "r") as file:
        times = int(file.readline().split(":")[1].replace(" ", ""))
        durations = int(file.readline().split(":")[1].replace(" ", ""))
    print(
        "Result for day6 part2: ",
        number_of_ways_to_beat_binary_search(times, durations, 14),
    )


def day7_part1(file_name: str = "data/day7.txt") -> None:
    ...


def day7_part2(file_name: str = "data/day7.txt") -> None:
    ...


def day8_part1(file_name: str = "data/day8.txt") -> None:
    ...


def day8_part2(file_name: str = "data/day8.txt") -> None:
    ...


def day9_part1(file_name: str = "data/day9.txt") -> None:
    ...


def day9_part2(file_name: str = "data/day9.txt") -> None:
    ...


def day10_part1(file_name: str = "data/day10.txt") -> None:
    ...


def day10_part2(file_name: str = "data/day10.txt") -> None:
    ...


def day11_part1(file_name: str = "data/day11.txt") -> None:
    ...


def day11_part2(file_name: str = "data/day11.txt") -> None:
    ...


def day12_part1(file_name: str = "data/day12.txt") -> None:
    ...


def day12_part2(file_name: str = "data/day12.txt") -> None:
    ...


def day13_part1(file_name: str = "data/day13.txt") -> None:
    ...


def day13_part2(file_name: str = "data/day13.txt") -> None:
    ...


def day14_part1(file_name: str = "data/day14.txt") -> None:
    ...


def day14_part2(file_name: str = "data/day14.txt") -> None:
    ...


def day15_part1(file_name: str = "data/day15.txt") -> None:
    ...


def day15_part2(file_name: str = "data/day15.txt") -> None:
    ...


def day16_part1(file_name: str = "data/day16.txt") -> None:
    ...


def day16_part2(file_name: str = "data/day16.txt") -> None:
    ...


def day17_part1(file_name: str = "data/day17.txt") -> None:
    ...


def day17_part2(file_name: str = "data/day17.txt") -> None:
    ...


def day18_part1(file_name: str = "data/day18.txt") -> None:
    ...


def day18_part2(file_name: str = "data/day18.txt") -> None:
    ...


def day19_part1(file_name: str = "data/day19.txt") -> None:
    ...


def day19_part2(file_name: str = "data/day19.txt") -> None:
    ...


def day20_part1(file_name: str = "data/day20.txt") -> None:
    ...


def day20_part2(file_name: str = "data/day20.txt") -> None:
    ...


def day21_part1(file_name: str = "data/day21.txt") -> None:
    ...


def day21_part2(file_name: str = "data/day21.txt") -> None:
    ...


def day22_part1(file_name: str = "data/day22.txt") -> None:
    ...


def day22_part2(file_name: str = "data/day22.txt") -> None:
    ...


def day23_part1(file_name: str = "data/day23.txt") -> None:
    ...


def day23_part2(file_name: str = "data/day23.txt") -> None:
    ...


def day24_part1(file_name: str = "data/day24.txt") -> None:
    ...


def day24_part2(file_name: str = "data/day24.txt") -> None:
    ...


def day25_part1(file_name: str = "data/day25.txt") -> None:
    ...


def day25_part2(file_name: str = "data/day25.txt") -> None:
    ...
