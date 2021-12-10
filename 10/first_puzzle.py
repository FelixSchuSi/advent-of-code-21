# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()

expected_closing_char_stack = []
OPENING_CHARS = ["(", "[", "{", "<"]
CLOSING_CHARS = [")", "]", "}", ">"]
SCORE_DICT = {")": 3, "]": 57, "}": 1197, ">": 25137}


def check_line(line: str) -> int:
    for char in line:
        if char in OPENING_CHARS:
            closing_char = CLOSING_CHARS[OPENING_CHARS.index(char)]
            expected_closing_char_stack.append(closing_char)
        if char in CLOSING_CHARS:
            if char != expected_closing_char_stack[-1]:
                expexted_char = expected_closing_char_stack[-1]
                print(f"Expected {expexted_char}, but found {char} instead.")
                return SCORE_DICT[char]
            else:
                expected_closing_char_stack.pop()
    return 0


print(sum([check_line(line) for line in lines]))
