from typing import Dict, List

# lines = open("example-input.txt", "r").readlines()
lines = open("input.txt", "r").readlines()

paths = []


def process_input(lines: List[str]) -> Dict[str, List[str]]:
    connections = {}
    for line in lines:
        start, end = line.strip().split("-")
        if connections.get(start):
            connections[start].append(end)
        else:
            connections[start] = [end]

        if connections.get(end):
            connections[end].append(start)
        else:
            connections[end] = [start]
    return connections


def calc_paths(connections: Dict[str, List[str]], _visited: List[str], pos: str):
    visited = _visited.copy()

    if pos in visited and pos.lower() == pos:
        if pos == "start":
            return
        small_caves_visited = list(filter(lambda c: c.lower() == c, visited))
        distinct_small_caves_visited = list(set(small_caves_visited))
        if len(small_caves_visited) > len(distinct_small_caves_visited):
            return  # One small cave has been visited twice already

    visited.append(pos)

    if pos == "end":
        paths.append(",".join(visited))
        return

    for next in connections[pos]:
        calc_paths(connections, visited, next)


connections = process_input(lines)
calc_paths(connections, _visited=[], pos="start")

# print("\n".join(paths))
print(len(paths))
