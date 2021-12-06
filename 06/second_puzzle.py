from typing import List


# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()


def parse_input(line: str):
    fishes_init = list(map(int, line.split(",")))
    fishes = [0] * 9
    for i in range(9):
        fishes[i] = len(list(filter(lambda fish: fish == i, fishes_init)))
    return fishes


def simulate_day(fishes: List[int]):
    number_of_fishes_at_zero = fishes[0]
    fishes.pop(0)
    fishes.append(0)
    fishes[6] += number_of_fishes_at_zero
    fishes[8] += number_of_fishes_at_zero
    return fishes


fishes = parse_input(lines[0])

print(f"Initial state: {fishes}")
for i in range(256):
    fishes = simulate_day(fishes)

print(sum(fishes))
