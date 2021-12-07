from typing import List

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()


def parse_input(lines: List[str]) -> List[int]:
    crabs = list(map(int, lines[0].split(",")))
    crabs.sort()
    return crabs


def find_median_position(crabs: List[int]) -> int:
    middle = int(len(crabs) / 2)
    if len(crabs) % 2 == 0:
        return int((crabs[middle] + crabs[middle - 1]) / 2)
    else:
        return int(crabs[middle])


def calc_fuel_consumption(crabs: List[int], position: int) -> int:
    distance = list(map(lambda crab: abs(crab - position), crabs))
    return int(sum(distance))


crabs = parse_input(lines)
best_position = find_median_position(crabs)
fuel_consumption = calc_fuel_consumption(crabs, best_position)
print(f"best_position {best_position} fuel_consumption {fuel_consumption}")
