# child nodes are defined in alphabetical order
graph = {"S": ["A", "B"],
         "B": ["S", "C"],
         "C": ["B", "A"],
         "A": ["C", "G", "S"],
         "G": ["A"]}


def breadth_first_search(g, start, end):
    visited, queue = [], [start]
    while queue:
        node = queue.pop(0)  # FiFo -> first element from queue is taken

        if node == end:
            visited.append(node)
            return visited

        if node not in visited:
            visited.append(node)
            successors = [i for i in g[node] if i not in visited]
            queue.extend(successors)

    return visited


if __name__ == '__main__':
    print(breadth_first_search(graph, "S", "G"))  # ['S', 'A', 'B', 'C', 'G']
