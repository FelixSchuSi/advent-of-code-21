# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()
count = len(lines)


def get_occurances_of_one_per_position(lines):
    occurances_of_one_per_position = []
    for line in lines:
        for index, char in enumerate(list(line.strip())):
            if len(occurances_of_one_per_position) < index + 1:
                occurances_of_one_per_position.append(0)
            occurances_of_one_per_position[index] += int(char)
    return occurances_of_one_per_position


def get_occurances_binary(lines, least_common):
    count = len(lines)
    occurances_of_one_per_position = get_occurances_of_one_per_position(lines)

    def get_most_common(x):
        return "1" if x >= (count / 2) else "0"

    def get_least_common(x):
        return "0" if x >= (count / 2) else "1"

    return "".join(
        list(
            map(
                get_least_common if least_common else get_most_common,
                occurances_of_one_per_position,
            )
        )
    )


def oxygen_filter(row, index_of_value, filter_value):
    return row[index_of_value] == filter_value


def get_measurement(least_common=False):
    file = list(map(lambda x: x.strip(), lines))

    for index_of_value in range(len(lines[0].strip())):
        occurances_binary = get_occurances_binary(file, least_common)

        # stop if a single result has been found
        if len(file) == 1:
            break

        file = list(
            filter(
                lambda x: oxygen_filter(
                    x, index_of_value, occurances_binary[index_of_value]
                ),
                file,
            )
        )

    binary = file[0]
    decimal = int(binary, 2)
    return decimal


oxygen = get_measurement()
c_o_two = get_measurement(least_common=True)
product = oxygen * c_o_two

print(f"oxygen: {oxygen} c_o_two: {c_o_two} product: {product}")
