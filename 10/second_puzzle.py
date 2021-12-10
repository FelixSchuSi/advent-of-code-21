from typing import Any, Dict, List

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()

OPENING_CHARS = ["(", "[", "{", "<"]
CLOSING_CHARS = [")", "]", "}", ">"]
SCORE_DICT = {")": 1, "]": 2, "}": 3, ">": 4}


def is_valid(line: str) -> List[Dict[str, Any]]:
    expected_closing_char_stack = []
    for char in line:
        if char in OPENING_CHARS:
            closing_char = CLOSING_CHARS[OPENING_CHARS.index(char)]
            expected_closing_char_stack.append(closing_char)
        if char in CLOSING_CHARS:
            if char != expected_closing_char_stack[-1]:
                return False
            else:
                expected_closing_char_stack.pop()
    return expected_closing_char_stack


def calc_score(expected_closing_char_stack: List[str]) -> int:
    score = 0
    for char in expected_closing_char_stack:
        score *= 5
        score += SCORE_DICT[char]
    return score


scores = []
for expected_closing_char_stack in map(is_valid, lines):
    if expected_closing_char_stack != False:
        expected_closing_char_stack.reverse()
        score = calc_score(expected_closing_char_stack)
        scores.append(score)

scores.sort()
print(scores[int(len(scores) / 2)])
