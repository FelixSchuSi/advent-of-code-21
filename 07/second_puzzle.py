from typing import List

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()


def parse_input(lines: List[str]) -> List[int]:
    crabs = list(map(int, lines[0].split(",")))
    crabs.sort()
    return crabs


def calc_fuel_consumption(crabs: List[int], position: int) -> int:
    distance = list(map(lambda crab: abs(crab - position), crabs))
    fuel_consumption = list(map(lambda d: calc_gauss_sum(d), distance))
    return int(sum(fuel_consumption))


def calc_gauss_sum(n: int) -> int:
    return int((n ** 2 + n) / 2)


crabs = parse_input(lines)
consumptions = list(
    map(lambda pos: calc_fuel_consumption(crabs, pos), list(range(max(crabs) + 1)))
)
print(min(consumptions))
