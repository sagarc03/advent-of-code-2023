from itertools import cycle


def get_direction(direction: str) -> cycle:
    return cycle(direction)


def get_map(map: str) -> dict[str, tuple[str, str]]:
    result: dict[str, tuple[str, str]] = {}
    for line in map.splitlines():
        key, value = line.split("=")
        l, r = value.strip()[1:-1].split(",")
        result[key.strip()] = (l.strip(), r.strip())
    return result
