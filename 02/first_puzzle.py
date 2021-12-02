position_horizontal = 0
position_depth = 0

for line in open("example-input.txt", "r").readlines():
    # for line in open("input.txt", "r").readlines():
    instruction, amount = line.strip().split(" ")
    if instruction == "forward":
        position_horizontal += int(amount)
    elif instruction == "down":
        position_depth += int(amount)
    elif instruction == "up":
        position_depth -= int(amount)
    else:
        print(f"Instruction unkown: {instruction}")

res = f"""horizontal position: {position_horizontal}
depth: {position_depth}
product: {position_horizontal * position_depth}
"""
print(res)
