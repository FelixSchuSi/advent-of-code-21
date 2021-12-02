position_horizontal = 0
position_depth = 0
aim = 0

# for line in open("example-input.txt", "r").readlines():
for line in open("input.txt", "r").readlines():
    instruction, amount = line.strip().split(" ")
    if instruction == "forward":
        position_horizontal += int(amount)
        position_depth += aim * int(amount)
    elif instruction == "down":
        aim += int(amount)
    elif instruction == "up":
        aim -= int(amount)
    else:
        print(f"Instruction unkown: {instruction}")

res = f"""horizontal position: {position_horizontal}
depth: {position_depth}
product: {position_horizontal * position_depth}
"""
print(res)
