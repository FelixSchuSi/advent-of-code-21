from typing import Dict, List, Tuple
from itertools import chain

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()
global_i = 0


def process_input(lines: List[str]) -> Tuple[str, List[Tuple[str, str]]]:
    initial_template = ""
    instructions = []
    for line in lines:
        if line.strip() == "":
            continue
        elif "->" in line:
            pos, char = line.strip().split(" -> ")
            instructions.append((pos, char))
        else:
            initial_template = line.strip()

    return (initial_template, instructions)


def apply_instructions(template: str, instructions: List[Tuple[str, str]]) -> str:
    result = template

    relevant_instructions = list(
        filter(lambda instr: instr[0] in template, instructions)
    )
    instruction_with_index = [
        (
            char,
            [
                index
                for index in range(len(template))
                if template.startswith(pos, index)
            ],
        )
        for pos, char in relevant_instructions
    ]
    flat_instructions = [
        (char, idx) for char, idx_list in instruction_with_index for idx in idx_list
    ]
    flat_instructions = sorted(flat_instructions, key=lambda x: x[1], reverse=True)
    for char, idx in flat_instructions:
        left = result[0 : idx + 1]
        right = result[idx + 1 : len(result)]
        res = "".join(chain(left, char, right))
        result = res
    return result


template, instructions = process_input(lines)
for i in range(10):
    global_i = i
    template = apply_instructions(template, instructions)

char_count = {}
for char in set(template):
    char_count[char] = 0
for char in template:
    char_count[char] += 1

print(char_count)
print(max(char_count.values()) - min(char_count.values()))
