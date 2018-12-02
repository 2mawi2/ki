# child nodes are defined in alphabetical order
graph = {"S": ["A", "B"],
         "B": ["S", "C"],
         "C": ["B", "A"],
         "A": ["C", "G", "S"],
         "G": ["A"]}

costs = {
    "BS": 1,
    "BC": 1,
    "CA": 2,
    "SA": 3,
    "AG": 2
}

heuristic = {
    "S": 5,
    "B": 3,
    "C": 2,
    "A": 2,
    "G": 0
}


def get_best_node(search_tree):
    """take node with min heuristic"""
    return sorted(search_tree, key=lambda x: heuristic[x])[0]


def greedy_best_first_search(g, start, end):
    visited, search_tree, cost = [], [start], 0
    while search_tree:

        node = get_best_node(search_tree)
        search_tree.remove(node)

        if node == end:
            visited.append(node)
            return visited

        visited.append(node)
        successors = g[node]  # [i for i in g[node] if i not in visited]
        search_tree.extend(successors)

    return visited


if __name__ == '__main__':
    print(greedy_best_first_search(graph, "S", "G"))  # ['S', 'A', 'G']
