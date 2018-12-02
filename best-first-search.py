
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


def deep_first_search(g, start):
    visited, stack, cost = [], [start], 0
    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            successors = [i for i in g[node] if i not in visited]
            stack.extend(successors)

    return visited


result = deep_first_search(graph, "S")  # ['S', 'A', 'G', 'C', 'B']
print(result)
