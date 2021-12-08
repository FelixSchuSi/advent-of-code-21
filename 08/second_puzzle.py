from typing import List
from itertools import chain

# WARNING: absolute dumpsterfire below
# I dont know how this trash produced the right output

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()

# dict of numbers where a one to one mapping between used segments and number exists
# key = number of used segment
# value = corresponding number
easy_numbers = {2: 1, 3: 7, 4: 4, 7: 8}


# Fill this list with known mappings
position_letter_mapping = [None] * 7


def parse_input(lines: List[str]) -> List[List[List[str]]]:
    result = []
    for line in lines:
        signals_and_output = line.split("|")
        signals, output = list(map(lambda x: x.strip().split(" "), signals_and_output))
        result.append([signals, output])

    return result


def get_letters_of_number_of_length(length: int, data: List[str]) -> List[List[str]]:
    return list(
        map(
            lambda x: [letter for letter in x], filter(lambda x: len(x) == length, data)
        )
    )


def find_candidates(data: List[List[str]]):
    position_letter_candidates = {
        "0": [],  # The letter of position 0 can be identified by looking at easy numbers 1 and 7
        "2_or_5": [],  # By looking at easy number 1 we know which letters map to positions 2 and 5
        "1_or_3": [],  # By looking at easy number 4 AND ABOVE MAPPING we know which letters map to positions 1 or 3
        "4_or_6": [],  # By looking at easy number 8 AND ABOVE MAPPING we know which letters map to positions 2 or 5
    }

    # find letter at position 0
    letters_of_number_one = get_letters_of_number_of_length(2, data)[0]
    letters_of_number_seven = get_letters_of_number_of_length(3, data)[0]

    letter_at_pos_0 = list(set(letters_of_number_one) ^ set(letters_of_number_seven))[0]
    position_letter_candidates["0"] = letter_at_pos_0
    position_letter_mapping[0] = letter_at_pos_0
    # find letters at position 2 and 5
    position_letter_candidates["2_or_5"] = letters_of_number_one

    # find letters at positiion 1 and 3
    letters_of_number_four = get_letters_of_number_of_length(4, data)[0]
    position_letter_candidates["1_or_3"] = list(
        set(letters_of_number_one) ^ set(letters_of_number_four)
    )

    # find letters at positiion 4 or 6
    letters_of_number_eight = get_letters_of_number_of_length(7, data)[0]

    position_letter_candidates["4_or_6"] = list(
        (set(letters_of_number_eight) ^ set(letters_of_number_four))
        ^ set([letter_at_pos_0])
    )

    return position_letter_candidates


def asdf(position_letter_candidates, data: List[str]):
    # position_letter_candidates = {
    #     "0": [],  # The letter of position 0 can be identified by looking at easy numbers 1 and 7
    #     "2_or_5": [],  # By looking at easy number 1 we know which letters map to positions 2 and 5
    #     "1_or_3": [],  # By looking at easy number 4 AND ABOVE MAPPING we know which letters map to positions 1 or 3
    #     "4_or_6": [],  # By looking at easy number 8 AND ABOVE MAPPING we know which letters map to positions 2 or 5
    # }
    # other numbers sorted by used segments
    # easy_numbers = { 1,  7,  4, 8}
    # 5: 2 | 3 | 5
    # 6: 0 | 6 | 9

    #  0000
    # 1    2
    # 1    2
    #  3333
    # 4    5
    # 4    5
    #  6666
    # find letters of number 2 by:
    # getting all inputs with length 5 -> lists of number 2,3,5
    # filter that list so that only entries remain, that have the letters of 4 AND 6 -> number 2
    letters_of_numbers_with_len_five = get_letters_of_number_of_length(
        5, data
    )  # letters of numbers 2,3,5
    letters_of_number_two = list(
        filter(
            lambda x: all([n in x for n in position_letter_candidates["4_or_6"]]),
            letters_of_numbers_with_len_five,
        )
    )[0]

    # find letter of pos 3:
    # letters of two and four NOT in one
    letters_of_number_one = get_letters_of_number_of_length(2, data)[0]
    letters_of_number_four = get_letters_of_number_of_length(4, data)[0]

    two_and_four = list(set(letters_of_number_two) & set(letters_of_number_four))
    two_and_four_not_one = list(
        filter(
            lambda x: True if x not in letters_of_number_one else False, two_and_four
        )
    )
    letter_of_pos_3 = two_and_four_not_one[0]
    position_letter_mapping[3] = letter_of_pos_3

    # find letter of pos 2:
    # two_and_four that is not pos3
    letter_of_pos_2 = list(filter(lambda x: x != letter_of_pos_3, two_and_four))[0]
    position_letter_mapping[2] = letter_of_pos_2

    # find letter of pos 1:
    # letters of four NOT in one AND NOT with letter of pos3
    letter_of_pos_1 = list(
        filter(
            lambda x: True
            if x not in letters_of_number_one and x != letter_of_pos_3
            else False,
            letters_of_number_four,
        )
    )[0]
    position_letter_mapping[1] = letter_of_pos_1

    # find letter of pos 5
    # letters of one that is not pos2
    letter_of_pos_5 = list(
        filter(lambda x: x != letter_of_pos_2, letters_of_number_one)
    )[0]
    position_letter_mapping[5] = letter_of_pos_5
    # find letter number five
    # all nubmers of len 5 with letter of pos 1
    letters_of_number_five = list(
        filter(
            lambda x: True if letter_of_pos_1 in x else False,
            letters_of_numbers_with_len_five,
        )
    )[0]

    #  0000
    # 1    2
    # 1    2
    #  3333
    # 4    5
    # 4    5
    #  6666
    # find letter of pos 6:
    # letters in 2 and 5 not po0 and not pos3
    # print(letters_of_number_five, letters_of_number_two)
    two_and_five = list(set(letters_of_number_five) & set(letters_of_number_two))
    letter_of_pos_6 = list(
        filter(
            lambda x: True
            if x not in [position_letter_mapping[0], position_letter_mapping[3]]
            else False,
            two_and_five,
        )
    )[0]
    position_letter_mapping[6] = letter_of_pos_6
    # find letter of pos 4
    # letters of two not 6,3,2,1
    letter_of_pos_4 = list(
        filter(
            lambda x: True
            if x
            not in [
                letter_of_pos_6,
                letter_of_pos_3,
                letter_of_pos_2,
                position_letter_mapping[0],
            ]
            else False,
            letters_of_number_two,
        )
    )[0]
    position_letter_mapping[4] = letter_of_pos_4
    return position_letter_mapping.copy()

    #  0000
    # 1    2
    # 1    2
    #  3333
    # 4    5
    # 4    5
    #  6666


dictt = {
    "012456": 0,
    "25": 1,
    "02346": 2,
    "02356": 3,
    "1235": 4,
    "01356": 5,
    "013456": 6,
    "025": 7,
    "0123456": 8,
    "012356": 9,
}


def number_by_letters(letters: str, mapping: List[str]) -> int:
    indexes = ""
    for letter in letters:
        indexes += str(mapping.index(letter))
    return dictt["".join(sorted([x for x in indexes]))]


parsed_lines = parse_input(lines)
sum = 0
for line in parsed_lines:
    data = list(chain(line[0], line[1]))
    candidates = find_candidates(data)
    mapping = asdf(candidates, data)
    res = int(
        "".join(
            list(map(lambda letters: str(number_by_letters(letters, mapping)), line[1]))
        )
    )
    print(res)
    sum += res

print(sum)
