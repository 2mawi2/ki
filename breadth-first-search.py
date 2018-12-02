# child nodes are defined in alphabetical order
graph = {"S": ["A", "B"],
         "B": ["S", "C"],
         "C": ["B", "A"],
         "A": ["C", "G", "S"],
         "G": ["A"]}


def breadth_first_search(g, start):
    visited, stack, cost = [], [start], 0
    while stack:
        node = stack.pop(0)  # FiFo -> first element from queue is taken

        if node not in visited:
            visited.append(node)
            successors = [i for i in g[node] if i not in visited]
            stack.extend(successors)

    return visited


if __name__ == '__main__':
    print(breadth_first_search(graph, "S"))  # ['S', 'A', 'B', 'C', 'G']
