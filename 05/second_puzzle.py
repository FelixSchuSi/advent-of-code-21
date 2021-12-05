from typing import List
import re

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()


def parse_input(lines: List[str]) -> List[List[int]]:
    vent_map = []
    for line in lines:
        start_x, start_y, end_x, end_y = list(
            map(int, re.split(",| -> ", line.strip()))
        )

        min_y, max_y = sorted([start_y, end_y])
        min_x, max_x = sorted([start_x, end_x])

        vent_map = ensure_vent_map_size(vent_map, max_x=max_x, max_y=max_y)

        if start_x == end_x:
            for i in list(range(min_y, max_y + 1)):
                vent_map[i][start_x] += 1
        elif start_y == end_y:
            for i in list(range(min_x, max_x + 1)):
                vent_map[start_y][i] += 1
        elif (max_y - min_y) == (max_x - min_x):
            # print(f"is 45 degree diagonal from {start_x},{start_y} to {end_x},{end_y}")
            distance = max_y - min_y
            positive_range = list(range(distance + 1))
            negative_range = list(map(lambda x: x * -1, positive_range))

            x_range = positive_range if start_x < end_x else negative_range
            y_range = positive_range if start_y < end_y else negative_range

            for i in positive_range:
                vent_map[start_y + y_range[i]][start_x + x_range[i]] += 1
        else:
            print(
                f"not a 45 degree diagonal from {start_x},{start_y} to {end_x},{end_y}"
            )
            continue

    return vent_map


def ensure_vent_map_size(
    initial_vent_map: List[List[int]], max_x: int, max_y: int
) -> List[List[int]]:
    vent_map = initial_vent_map

    column_length = 0
    if len(vent_map) != 0:
        column_length: int = max(list(map(lambda row: len(row), vent_map)))

    for _ in range(max_y - len(vent_map) + 1):
        vent_map.append([0] * column_length)

    for row in vent_map:
        row.extend([0] * (max_x - len(row) + 1))

    # Accessing value at max index to assert that size is correct
    vent_map[max_y][max_x]
    return vent_map


vent_map = parse_input(lines)

flat_vent_map_without_ones = [
    0 if cell <= 1 else cell for row in vent_map for cell in row
]
number_of_overlapping_vents = len(
    list(filter(lambda x: x != 0, flat_vent_map_without_ones))
)
print(number_of_overlapping_vents)
