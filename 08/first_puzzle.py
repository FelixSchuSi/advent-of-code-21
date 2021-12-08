from types import resolve_bases
from typing import List

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()

# dict of numbers where a one to one mapping between used segments and number exists
# key = number of used segment
# value = corresponding number
easy_numbers = {2: 1, 3: 7, 4: 4, 7: 8}

# other numbers sorted by used segments
# 5: 2 | 3 | 5
# 6: 0 | 6 | 9


def parse_input(lines: List[str]) -> List[List[str]]:
    result = []
    for line in lines:
        signals_and_output = line.split("|")
        signals, output = list(map(lambda x: x.strip().split(" "), signals_and_output))
        result.append([signals, output])

    return result


def count_number_of_easy_numbers(parsed_lines: List[List[str]]) -> int:
    count = 0
    for line in parsed_lines:
        signals, output = line
        mapped = list(map(lambda x: easy_numbers.get(len(x)) or -1, output))
        count += len(list(filter(lambda x: x != -1, mapped)))

    return count


parsed_lines = parse_input(lines)
count = count_number_of_easy_numbers(parsed_lines)
print(count)
