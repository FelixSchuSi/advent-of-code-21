count = 0
# occurances_of_one_per_position = [0, 0, 0, 0, 0]
occurances_of_one_per_position = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 111001110000
# for line in open("example-input.txt", "r").readlines():
for line in open("input.txt", "r").readlines():
    count += 1
    for index, char in enumerate(list(line.strip())):
        occurances_of_one_per_position[index] += int(char)

gamma_binary = "".join(
    list(
        map(
            lambda x: "1" if x > int(count / 2) else "0", occurances_of_one_per_position
        )
    )
)
gamma_decimal = int(gamma_binary, 2)

epsilon_binary = "".join(
    list(
        map(
            lambda x: "0" if x > int(count / 2) else "1", occurances_of_one_per_position
        )
    )
)
epsilon_decimal = int(epsilon_binary, 2)
print(gamma_decimal, epsilon_decimal, gamma_decimal * epsilon_decimal)
