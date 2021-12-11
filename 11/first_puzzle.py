from typing import List
import pandas as pd
from pandas.core.frame import DataFrame

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()

flashes = 0


def process_input(lines: List[str]) -> DataFrame:
    parsed = [[int(char) for char in line.strip()] for line in lines]
    return DataFrame(parsed)


def simulate_step(initial_octopuses: DataFrame) -> DataFrame:
    octopuses = initial_octopuses.copy(deep=True)
    octopuses += 1
    octopuses = flash(octopuses)
    return octopuses


OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def flash(initial_octopuses: DataFrame) -> DataFrame:
    global flashes
    octopuses = initial_octopuses.copy(deep=True)
    for y in range(octopuses[0].size):
        for x in range(octopuses.columns.size):
            if octopuses.iloc[y, x] > 9:
                for y_offset, x_offset in OFFSETS:
                    y_new, x_new = (y_offset + y, x_offset + x)
                    if y_new > (octopuses[0].size - 1):
                        continue
                    if x_new > (octopuses.columns.size - 1):
                        continue
                    if x_new < 0 or y_new < 0:
                        continue
                    if octopuses.iloc[y_new, x_new] != -1:
                        octopuses.iloc[y_new, x_new] += 1
                octopuses.iloc[y, x] = -1
                flashes += 1

    while not (octopuses <= 9).all().all():
        octopuses = flash(octopuses)

    octopuses[octopuses == -1] = 0
    return octopuses


octopuses = process_input(lines)

for _ in range(100):
    octopuses = simulate_step(octopuses)

print(octopuses)
print(flashes)
