class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []

        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = []

        self.adjacency_list[vertex1].append(vertex2)

    def get_vertex_count(self):
        return len(self.adjacency_list)

    def get_neighbours(self, vertex):
        return self.adjacency_list[vertex]

    def get_neighbours_count(self, vertex):
        return len(self.adjacency_list[vertex])

    def display(self):
        for vertex, edge in self.adjacency_list.items():
            print(vertex, " -> ", edge)


def topologicalSort(graph, visited, current, stack):

    visited[current] = True

    for i in range(graph.get_neighbours_count(current)):
        neighbour = graph.get_neighbours(current)[i]
        if not visited[neighbour]:
            topologicalSort(graph, visited, neighbour, stack)

    stack.append(current)


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(5, 0)
    graph.add_edge(5, 2)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)

    graph.display()

    visited = [False for i in range(graph.get_vertex_count())]
    stack = []

    for i in range(graph.get_vertex_count()):
        if not visited[i]:
            topologicalSort(graph, visited, i, stack)

    while stack:
        print(stack.pop())
