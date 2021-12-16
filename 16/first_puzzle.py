from typing import Dict, List, Tuple
from itertools import chain

lines = open("example-input.txt", "r").readlines()
# lines = open("input.txt", "r").readlines()


def process_input(lines: List[str]) -> Tuple[int, int, List[str]]:
    line = bin(int(lines[0].strip(), 16))[2:]
    version = int(line[0:3], base=2)
    id = int(line[3:6], base=2)
    payload = line[6:]

    return version, id, payload


def process_literal(payload: List[str]) -> int:
    payload = [payload[0 + i : 5 + i] for i in range(0, len(payload), 5)]
    payload = list(filter(lambda x: not (x == "0" * len(x) and len(x) < 5), payload))
    literal = [part[1:] for part in payload]
    return int("".join(literal), 2)


def process_operator(payload: List[str]) -> int:
    length_type_id = payload[0]
    payload = payload[1:]
    if length_type_id == 0:
        
    return


version, id, payload = process_input(lines)
if id == 4:
    literal = process_literal(payload)
    print(literal)
else:
    operator = process_operator(payload)
