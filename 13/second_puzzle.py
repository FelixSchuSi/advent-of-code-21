from typing import Dict, List, Tuple
import pandas as pd
from pandas.core.frame import DataFrame

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()


def process_input(lines: List[str]) -> Tuple[List[List[str]], List[Tuple[str, int]]]:
    dots = []
    folds = []
    max_x = 0
    max_y = 0
    for line in lines:
        if line.strip() == "":
            continue
        if line.startswith("fold along "):
            axis, index = line.replace("fold along ", "").split("=")
            folds.append((axis, int(index)))
            continue
        x, y = [int(char) for char in line.strip().split(",")]
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        dots.append((x, y))

    paper = [["⬛" for cell in range(max_x + 1)] for row in range(max_y + 1)]

    for x, y in dots:
        paper[y][x] = "⬜"
    return paper, folds


def fold_paper(paper: List[List[str]], fold: Tuple[str, int]) -> List[List[str]]:
    axis, index = fold
    first_half = []
    second_half = []
    new_paper = []
    if axis == "y":
        paper.pop(index)
        first_half = paper[0:index]
        second_half = paper[index : len(paper)]
        second_half = list(reversed(second_half))
        max_y = max(len(first_half), len(second_half))
        max_x = max(len(first_half[0]), len(second_half[0]))
        new_paper = [["⬛" for cell in range(max_x)] for row in range(max_y)]

        for y in range(max_y):
            for x in range(max_x):
                first, second = "⬛", "⬛"
                try:
                    first = first_half[len(first_half) - 1 - y][x]
                except:
                    pass
                try:
                    second = second_half[len(second_half) - 1 - y][x]
                except:
                    pass
                black = first == "⬛" and second == "⬛"
                new_paper[len(new_paper) - 1 - y][x] = "⬛" if black else "⬜"
    else:
        for row in paper:
            row.pop(index)
        first_half = [row[0:index] for row in paper]
        end = len(row)
        second_half = [row[index:end] for row in paper]
        second_half = [list(reversed(row)) for row in second_half]
        max_y = max(len(first_half), len(second_half))
        max_x = max(len(first_half[0]), len(second_half[0]))
        new_paper = [["⬛" for cell in range(max_x)] for row in range(max_y)]

        for y in range(max_y):
            for x in range(max_x):
                first, second = "⬛", "⬛"
                try:
                    first = first_half[y][len(first_half[0]) - 1 - x]
                except:
                    pass
                try:
                    second = second_half[y][len(second_half[0]) - 1 - x]
                except:
                    pass
                black = first == "⬛" and second == "⬛"
                new_paper[y][len(new_paper[0]) - 1 - x] = "⬛" if black else "⬜"
    return new_paper


def print_paper(paper):
    for row in paper:
        print("".join(row))
    print()


paper, folds = process_input(lines)
for fold in folds:
    paper = fold_paper(paper, fold)

print_paper(paper)
