# child nodes are defined in alphabetical order
graph = {"S": ["A", "B"],
         "B": ["S", "C"],
         "C": ["B", "A"],
         "A": ["C", "G", "S"],
         "G": ["A"]}


def deep_first_search(g, start):
    visited, stack, cost = [], [start], 0
    while stack:
        node = stack.pop()  # LiFo -> deeper nodes are prioritized

        if node not in visited:
            visited.append(node)
            successors = [i for i in g[node] if i not in visited]
            stack.extend(successors)

    return visited


if __name__ == '__main__':
    print(deep_first_search(graph, "S"))  # ['S', 'B', 'C', 'A', 'G']

