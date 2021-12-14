from collections import Counter
from functools import lru_cache
from typing import Dict, Tuple
import time


def solve(template: str, rules: Dict[Tuple[str, str], str], n: int) -> int:
    if not len(template):
        return 0

    @lru_cache(maxsize=None)
    def count_between(left: str, right: str, n: int) -> Counter:
        if n == 0:
            return Counter(left)
        mid = rules[(left, right)]
        return count_between(left, mid, n - 1) + count_between(mid, right, n - 1)

    counts = Counter(template[-1])
    for left, right in zip(template, template[1:]):
        counts += count_between(left, right, n)
    lowest, *_, highest = sorted(counts.values())

    return highest - lowest


def run(data_s: str) -> Tuple[int, int]:
    template, rules_s = data_s.split("\n\n")
    rules = {}
    for rule in rules_s.splitlines():
        left_right, _, mid = rule.partition(" -> ")
        left, right = tuple(left_right)
        rules[(left, right)] = mid

    part1 = solve(template, rules, 10)
    part2 = solve(template, rules, 40)

    return part1, part2


# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()

startTime = time.time()
print(run("".join(lines)))
print(f"Executed in {time.time() - startTime} seconds")
# Executed in 0.017041683197021484 seconds with cache
