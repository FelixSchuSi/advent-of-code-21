from typing import List
from itertools import chain

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()


def parse_input(lines: List[str]) -> List[List[int]]:
    result = []
    for line in lines:
        result.append([int(height) for height in line.strip()])
    return result


def get_low_points(smoke_map: List[List[int]]) -> List[List[bool]]:
    low_poimts_map = [row.copy() for row in smoke_map]
    smoke_map_height = len(smoke_map)
    smoke_map_width = len(smoke_map[0])

    for y in range(smoke_map_height):
        for x in range(smoke_map_width):
            offsets = get_offsets(y, x, smoke_map_height, smoke_map_width)
            low_poimts_map[y][x] = is_low_point(y, x, smoke_map, offsets)

    return low_poimts_map


def get_offsets(y: int, x: int, smoke_map_height: int, smoke_map_width: int):
    offsets = []

    if y >= 1:  # top
        offsets.append([0, -1])

    if y < smoke_map_height - 1:  # down
        offsets.append([0, 1])

    if x >= 1:  # left
        offsets.append([-1, 0])

    if x < smoke_map_width - 1:  # right
        offsets.append([1, 0])

    return offsets


def is_low_point(y: int, x: int, smoke_map: List[List[int]], offsets):
    value = smoke_map[y][x]
    lower = []
    for x_offset, y_offset in offsets:
        lower.append(smoke_map[y + y_offset][x + x_offset] > value)
    return all(lower)


def get_risk_level(smoke_map, low_point_map):
    smoke_map_height = len(smoke_map)
    smoke_map_width = len(smoke_map[0])

    result = 0

    for y in range(smoke_map_height):
        for x in range(smoke_map_width):
            if low_point_map[y][x]:
                result += smoke_map[y][x] + 1

    return result


smoke_map = parse_input(lines)
low_point_map = get_low_points(smoke_map)
print(get_risk_level(smoke_map, low_point_map))
