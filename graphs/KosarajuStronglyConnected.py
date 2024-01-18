from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.adjacency_list = defaultdict(list)

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = []

        self.adjacency_list[vertex1].append(vertex2)

    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(vertex, " -> ", edges)


def topological_sort(graph, current, visited, stack):
    visited[current] = True

    for neighbour in graph.adjacency_list[current]:
        if not visited[neighbour]:
            topological_sort(graph, neighbour, visited, stack)

    stack.append(current)


def dfs(graph, current, visited, path):
    visited[current] = True
    path += str(current)
    for neighbour in graph.adjacency_list[current]:
        if not visited[neighbour]:
            path = dfs(graph, neighbour, visited, path)

    return path


def kosaraju(graph):
    stack = []
    visited = {vertex: False for vertex in graph.adjacency_list}
    topological_sort(graph, 0, visited, stack)

    transposedGraph = Graph()

    for vertex in graph.adjacency_list:
        visited[vertex] = False
        for neighbour in graph.adjacency_list[vertex]:
            transposedGraph.add_edge(neighbour, vertex)

    print("Transposed Graph")
    transposedGraph.display()

    # Perform dfs on transposed Graph with starting vertices from the stack
    # obtained from topological sort
    while stack:
        top = stack.pop()
        if not visited[top]:
            path = ""
            stronglyConnected = dfs(transposedGraph,  top, visited, path)
            print(stronglyConnected)


graph = Graph()
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 0)
graph.add_edge(2, 1)
graph.add_edge(3, 4)
graph.display()

kosaraju(graph)
