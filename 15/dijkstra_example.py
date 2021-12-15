# Taken from https://likegeeks.com/python-dijkstras-algorithm/
from numpy import inf

graph = {
    "A": {"C": 5, "D": 1, "E": 2},
    "B": {"H": 1, "G": 3},
    "C": {"I": 2, "D": 3, "A": 5},
    "D": {"C": 3, "A": 1, "H": 2},
    "E": {"A": 2, "F": 3},
    "F": {"E": 3, "G": 1},
    "G": {"F": 1, "B": 3, "H": 2},
    "H": {"I": 2, "D": 2, "B": 1, "G": 2},
    "I": {"C": 2, "H": 2},
}
costs = {
    "A": 0,
    "B": inf,
    "C": inf,
    "D": inf,
    "E": inf,
    "F": inf,
    "G": inf,
    "H": inf,
    "I": inf,
}
parents = {}


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


result = search("A", "B", graph, costs, parents)
print(result)


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


print("parent dictionary={}".format(result))
print("longest path={}".format(backpedal("A", "B", result)))
