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
        return

    visited.append(pos)

    if pos == "end":
        paths.append(",".join(visited))
        return

    for next in connections[pos]:
        calc_paths(connections, visited, next)


connections = process_input(lines)
calc_paths(connections, _visited=[], pos="start")

print(len(paths))
