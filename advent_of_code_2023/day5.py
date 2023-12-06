from typing import Iterable, LiteralString, NamedTuple, Self


def get_seeds(seeds: str) -> list[int]:
    return [int(x) for x in seeds.split()[1:]]


def get_seeds_interval(seeds: str) -> list[tuple[int, int]]:
    s = [int(x) for x in seeds.split()[1:]]
    return [(start, start + rng) for start, rng in zip(s[::2], s[1::2])]


class MapTuple(NamedTuple):
    destination_range_start: int
    source_range_start: int
    range_length: int


class Maps:
    def __init__(self, maps: list[MapTuple]) -> None:
        self._maps = maps
        self._maps.sort(key=lambda x: x.source_range_start)

    def apply_for_value(self, source: int) -> int:
        for each in self._maps:
            if (
                each.source_range_start <= source
                and source < each.source_range_start + each.range_length
            ):
                return each.destination_range_start + (source - each.source_range_start)
        return source

    def apply_for_ranges(self, ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
        result = []

        for map in self._maps:
            soruce_end = map.source_range_start + map.range_length
            next_range = []
            while ranges:
                start, end = ranges.pop()
                before = (start, min(end, map.source_range_start))
                inter = (
                    max(start, map.source_range_start),
                    min(soruce_end, end),
                )
                after = (max(start, soruce_end), end)
                if before[1] > before[0]:
                    next_range.append(before)
                if inter[1] > inter[0]:
                    result.append(
                        (
                            inter[0]
                            - map.source_range_start
                            + map.destination_range_start,
                            inter[1]
                            - map.source_range_start
                            + map.destination_range_start,
                        )
                    )
                if after[1] > after[0]:
                    next_range.append(after)
            ranges = next_range

        return result + ranges


def get_maps(maps_data: list[str] | list[LiteralString]) -> list[Maps]:
    maps = []
    for each in maps_data:
        temp = []
        for line in each.strip().split("\n")[1:]:
            x = line.strip().split()
            temp.append(MapTuple(int(x[0]), int(x[1]), int(x[2])))
        maps.append(Maps(temp))
    return maps
