# child nodes are defined in alphabetical order
graph = {"S": ["A", "B"],
         "B": ["S", "C"],
         "C": ["B", "A"],
         "A": ["C", "G", "S"],
         "G": ["A"]}


def depth_first_search(g, start, end):
    visited, stack = [], [start]
    while stack:
        node = stack.pop()  # LiFo -> deeper nodes are prioritized

        if node == end:
            visited.append(node)
            return visited

        if node not in visited:
            visited.append(node)
            successors = [i for i in g[node] if i not in visited]
            stack.extend(successors)

    return visited


if __name__ == '__main__':
    print(depth_first_search(graph, "S", "G"))  # ['S', 'B', 'C', 'A', 'G']
