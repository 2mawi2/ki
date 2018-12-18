# child nodes are defined in alphabetical order
from dataclasses import dataclass

graph = {"S": ["A", "B"],
         "B": ["S", "C"],
         "C": ["B", "A"],
         "A": ["C", "G", "S"],
         "G": ["A"]}

costs = {
    "BS": 1,
    "BC": 1,
    "AC": 2,
    "AS": 3,
    "AG": 2
}

heuristic = {
    "S": 5,
    "B": 3,
    "C": 2,
    "A": 2,
    "G": 0
}


@dataclass
class Node:
    name: str
    cost: int
    visited: [str]


def get_path_cost(path):
    total_cost = 0
    for i in range(len(path) - 1):
        p = "".join(sorted(path[i] + path[i + 1]))
        cost = costs[p]
        total_cost += cost
    return total_cost


def get_best_node(search_tree):
    return sorted(search_tree, key=lambda x: x.cost)[0]


def uniform_cost_search(g, start, end):
    visited, search_tree, cost = [], [Node(name=start, cost=0, visited=[])], 0
    while search_tree:

        node = get_best_node(search_tree)
        search_tree.remove(node)
        visited = node.visited

        if node == end:
            visited.append(node.name)
            return visited

        visited.append(node.name)
        successors = [i for i in graph[node.name] if i not in visited]
        c = [Node(name=i, cost=get_path_cost(i.visited + [i]), visited=visited) for i in successors]
        search_tree.extend(c)

    return visited


if __name__ == '__main__':
    print(uniform_cost_search(graph, "S", "G"))  # ['S', 'A', 'G']
