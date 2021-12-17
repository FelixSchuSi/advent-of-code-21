from typing import Dict, List, Tuple
from itertools import chain

lines = open("example-input.txt", "r").readlines()
# lines = open("input.txt", "r").readlines()


def process_input(lines: List[str]) -> Tuple[Tuple[int, int]]:
    line = lines[0].strip().split("target area: ")[1]
    x_limits, y_limits = line.split(", ")
    x_max, x_min = [int(limit) for limit in x_limits[2:].split("..")]
    y_max, y_min = [int(limit) for limit in y_limits[2:].split("..")]
    return (x_max, x_min), (y_max, y_min)


x_limits, y_limits = process_input(lines)
print(x_limits, y_limits)
