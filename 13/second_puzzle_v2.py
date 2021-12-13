import numpy as np

with open("input.txt", "rt") as file:
    dots = []
    for line in file:
        if line == "\n":
            break
        x, y = line.rstrip().split(",")
        dots += [(int(x), int(y))]

    instructions = []
    for line in file:
        my_instruction = line.split()
        my_instruction = my_instruction[-1].split("=")
        axis, pos = my_instruction
        instructions += [(axis, int(pos))]

max_x = max(x for x, y in dots)
max_y = max(y for x, y in dots)

paper = np.zeros(shape=(max_y + 1, max_x + 1), dtype="bool")
for x, y in dots:
    paper[y, x] = True

for step, (axis, pos) in enumerate(instructions):

    if axis == "x":
        half_1 = paper[..., 0:pos]
        half_2 = np.flip(paper[..., pos + 1 :], axis=1)
        diff = half_1.shape[1] - half_2.shape[1]

        padding = np.zeros(shape=(half_1.shape[0], abs(diff)), dtype="bool")
        if diff > 0:
            half_2 = np.append(padding, half_2, axis=1)
        if diff < 0:
            half_1 = np.append(padding, half_1, axis=1)

    elif axis == "y":
        half_1 = paper[0:pos, ...]
        half_2 = np.flip(paper[pos + 1 :, ...], axis=0)

        diff = half_1.shape[0] - half_2.shape[0]
        padding = np.zeros(shape=(abs(diff), half_1.shape[1]), dtype="bool")
        if diff > 0:
            half_2 = np.append(padding, half_2, axis=0)
        if diff < 0:
            half_1 = np.append(padding, half_1, axis=0)

    paper = half_1 | half_2

output = ""
for row in paper:
    line = ""
    for dot in row:
        line += "⬜" if dot else "⬛"
    output += line + "\n"

print(f"\nPart 2:\n{output}")
