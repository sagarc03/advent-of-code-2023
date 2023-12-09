from math import lcm

import pytest

from advent_of_code_2023.day8 import get_direction, get_map


@pytest.mark.parametrize(
    "test_data,result",
    [
        (
            """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""",
            2,
        ),
        (
            """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""",
            6,
        ),
    ],
)
def test_find_ZZZ(test_data: str, result: int) -> None:
    directions = get_direction(test_data.split("\n\n")[0])
    map = get_map(test_data.split("\n\n")[1])

    node = "AAA"
    steps = 0

    for direction in directions:
        if direction == "L":
            node = map[node][0]
        else:
            node = map[node][1]
        steps += 1
        if node == "ZZZ":
            break

    assert steps == result


@pytest.mark.parametrize(
    "test_data,result",
    [
        (
            """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""",
            6,
        ),
    ],
)
def test_find_Z(test_data: str, result: int) -> None:
    directions = get_direction(test_data.split("\n\n")[0])
    map = get_map(test_data.split("\n\n")[1])
    print(test_data.split("\n\n"))

    steps = 0
    nodes = [x for x in map.keys() if x.endswith("A")]
    n = len(nodes)
    T = {}
    for direction in directions:
        if direction == "L":
            d = 0
        else:
            d = 1
        for i in range(n):
            nodes[i] = map[nodes[i]][d]
        steps += 1

        for i in range(n):
            if nodes[i].endswith("Z"):
                T[i] = steps
        if len(T) == n:
            break

    assert lcm(*T.values()) == result
