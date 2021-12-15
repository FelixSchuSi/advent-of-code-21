from functools import total_ordering
from typing import Dict, List
from numpy import inf


def get_neighbours(x: int, y: int, height: int, width: int):
    neighbours = []
    if y >= 1:  # top
        neighbours.append([x, y - 1])
    if y < height - 1:  # down
        neighbours.append([x, y + 1])
    if x >= 1:  # left
        neighbours.append([x - 1, y])
    if x < width - 1:  # right
        neighbours.append([x + 1, y])
    return neighbours


def build_graph(lines: List[str]) -> Dict:
    graph = {}
    costs = {}
    for y, row in enumerate(lines):
        for x, weight in enumerate(row):
            costs[(x, y)] = inf
            neighbours = get_neighbours(x, y, len(lines), len(row))
            for neighbour_x, neighbour_y in neighbours:
                if not graph.get((neighbour_x, neighbour_y)):
                    graph[(neighbour_x, neighbour_y)] = {}
                graph[(neighbour_x, neighbour_y)][(x, y)] = int(weight)
    costs[(0, 0)] = 0
    return graph, costs


def search(source, target, graph, costs, parents):
    nextNode = source
    while nextNode != target:
        for neighbor in graph[nextNode]:
            if graph[nextNode][neighbor] + costs[nextNode] < costs[neighbor]:
                costs[neighbor] = graph[nextNode][neighbor] + costs[nextNode]
                parents[neighbor] = nextNode
            del graph[neighbor][nextNode]
        del costs[nextNode]
        nextNode = min(costs, key=costs.get)
    return parents


def backpedal(source, target, searchResult):
    node = target
    backpath = [target]
    path = []
    while node != source:
        backpath.append(searchResult[node])
        node = searchResult[node]
    for i in range(len(backpath)):
        path.append(backpath[-i - 1])
    return path


# lines = [line.strip() for line in open("example-input.txt", "r").readlines()]
lines = [line.strip() for line in open("input.txt", "r").readlines()]

graph, costs = build_graph(lines)
parents = {}
src = (0, 0)
target = (len(lines) - 1, len(lines[0]) - 1)

result = search(src, target, graph, costs, parents)

shortest_path = backpedal(src, target, result)
# print(f"shortest path={shortest_path}")

graph, _ = build_graph(lines)
total_cost = 0
for i, (x, y) in enumerate(shortest_path):
    if i == 0:
        continue
    prev_x, prev_y = shortest_path[i - 1]
    total_cost += graph[(prev_x, prev_y)][(x, y)]
print(total_cost)
