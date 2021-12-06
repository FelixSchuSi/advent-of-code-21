from typing import List


# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()


def parse_input(line: str) -> List[int]:
    return list(map(int, line.split(",")))


def simulate_day(fishes: List[int]) -> List[int]:
    aged_fishes = list(map(lambda fish: fish - 1, fishes))
    number_of_new_fishes = len(list(filter(lambda fish: fish == -1, aged_fishes)))
    aged_fishes_and_new_fishes = aged_fishes
    aged_fishes_and_new_fishes.extend([8] * number_of_new_fishes)
    return list(map(lambda fish: 6 if fish == -1 else fish, aged_fishes_and_new_fishes))


fishes = parse_input(lines[0])

print(f"Initial state: {fishes}")
for i in range(80):
    fishes = simulate_day(fishes)
    # print(f"After {i+1} days: {fishes}")

print(len(fishes))
