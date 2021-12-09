from typing import List, Tuple
from itertools import chain
import numpy as np

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()

basins = []


def parse_input(lines: List[str]) -> List[List[int]]:
    result = []
    for line in lines:
        result.append([int(height) for height in line.strip()])
    return result


def get_basins_and_calc_score(smoke_map: List[List[int]]) -> List[List[bool]]:
    smoke_map_height = len(smoke_map)
    smoke_map_width = len(smoke_map[0])

    for y in range(smoke_map_height):
        for x in range(smoke_map_width):
            if smoke_map[y][x] != 9 and not is_part_of_existing_basin(y, x):
                explore_basin(y, x, smoke_map_height, smoke_map_width, smoke_map)

    sizes = []
    smoke_map_array = np.array(smoke_map)
    for basin in basins:
        mask = np.array(basin)
        sizes.append(len(smoke_map_array[mask]))

    sizes = sorted(sizes)
    print(sizes[-1], sizes[-2], sizes[-3])
    return sizes[-1] * sizes[-2] * sizes[-3]


def explore_basin(
    y: int, x: int, smoke_map_height: int, smoke_map_width: int, smoke_map
):
    basin = [[False] * len(row) for row in smoke_map]
    basin_fields_not_visited = []  # Field is visited when all neighbours have been seen
    # Add initial coordinate to basin
    basin[y][x] = True

    basin_fields_not_visited.append((y, x))

    while len(basin_fields_not_visited) > 0:
        visit_next_basin_field(
            smoke_map_height,
            smoke_map_width,
            smoke_map,
            basin,
            basin_fields_not_visited,
        )

    basins.append(basin)


def visit_next_basin_field(
    smoke_map_height: int,
    smoke_map_width: int,
    smoke_map: List[List[int]],
    basin: List[List[bool]],
    basin_fields_not_visited: List[Tuple[int]],
):
    y, x = basin_fields_not_visited.pop(0)

    # up
    for i in range(1, y + 1):
        new_y = y - i
        if smoke_map[new_y][x] != 9 and basin[new_y][x] == False:
            basin[new_y][x] = True
            basin_fields_not_visited.append((new_y, x))
        else:
            break

    # down
    for new_y in range(y + 1, smoke_map_height):
        if smoke_map[new_y][x] != 9 and basin[new_y][x] == False:
            basin[new_y][x] = True
            basin_fields_not_visited.append((new_y, x))
        else:
            break

    # left
    for i in range(1, x + 1):
        new_x = x - i
        if smoke_map[y][new_x] != 9 and basin[y][new_x] == False:
            basin[y][new_x] = True
            basin_fields_not_visited.append((y, new_x))
        else:
            break

    # right
    for new_x in range(x + 1, smoke_map_width):
        if smoke_map[y][new_x] != 9 and basin[y][new_x] == False:
            basin[y][new_x] = True
            basin_fields_not_visited.append((y, new_x))
        else:
            break


def is_part_of_existing_basin(y: int, x: int) -> bool:
    for basin in basins:
        if basin[y][x] == True:
            return True
    return False


smoke_map = parse_input(lines)
score = get_basins_and_calc_score(smoke_map)
print(score)
