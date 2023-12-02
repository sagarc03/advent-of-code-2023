from collections import defaultdict


def _game_dict(game_str: str) -> dict[str, int]:
    game_data: dict[str, int] = {}
    for cube_draw in game_str.strip().split(","):
        c = cube_draw.strip().split(" ")
        game_data[c[1]] = int(c[0])
    return game_data


def process_game_data(input_data: str) -> tuple[int, list[dict[str, int]]]:
    name_gamedata = input_data.strip().split(":")
    name_gamedata[-1].strip().split(";")

    return (
        int(name_gamedata[0].split(" ")[-1]),
        [_game_dict(x) for x in name_gamedata[-1].strip().split(";")],
    )


def _is_draw_possible(
    draw: dict[str, int], available_cubes: defaultdict[str, int]
) -> bool:
    for cube, value in draw.items():
        if available_cubes[cube] < value:
            return False
    return True


def is_game_possible(
    game_data: list[dict[str, int]], available_cubes: defaultdict[str, int]
) -> bool:
    for draw in game_data:
        if not _is_draw_possible(draw, available_cubes):
            return False
    return True


def _min_cubes_to_make_game_possible(
    game_data: list[dict[str, int]]
) -> defaultdict[str, int]:
    cubes: defaultdict[str, int] = defaultdict(int)
    for draw in game_data:
        for key, value in draw.items():
            if cubes[key] < value:
                cubes[key] = value
    return cubes


def get_power_set(game_data: list[dict[str, int]]) -> int:
    result = 1
    for _, value in _min_cubes_to_make_game_possible(game_data).items():
        result *= value
    return result
