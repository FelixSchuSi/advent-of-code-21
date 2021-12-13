from typing import Dict, List, Tuple
import pandas as pd
from pandas.core.frame import DataFrame

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()


def process_input(lines: List[str]) -> Tuple[DataFrame, List[Tuple[str, int]]]:
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

    paper = [[False for cell in range(max_x + 1)] for row in range(max_y + 1)]

    for x, y in dots:
        paper[y][x] = True
    return DataFrame(paper), folds


def fold_paper(paper: DataFrame, fold: Tuple[str, int]) -> List[List[bool]]:
    axis, index = fold
    if axis == "y":
        paper = DataFrame(paper.drop([index]).values.tolist())
        first_half = paper.iloc[:index, 0:]
        second_half = paper.iloc[index:, 0:]
        reversed = DataFrame(second_half.iloc[::-1].values.tolist())
        return first_half | reversed
    else:
        paper = DataFrame(paper.drop([index], axis=1).values.tolist())
        first_half = paper.iloc[0:, :index]
        second_half = DataFrame(paper.iloc[0:, index:].values.tolist())
        reversed = DataFrame(second_half.iloc[::, ::-1].values.tolist())
        return first_half | reversed


paper, folds = process_input(lines)
# for fold in folds:
paper = fold_paper(paper, folds[0])

print(sum(paper[paper == True].count()))
