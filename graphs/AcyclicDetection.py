class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = []

        self.adjacency_list[vertex1].append(vertex2)

    def getVertexCount(self):
        return len(self.adjacency_list)

    def display(self):
        for vertex, edge in self.adjacency_list.items():
            print(vertex, " -> ", edge)


def dfs(graph, visited, current, rec):

    visited[current] = True
    rec[current] = True

    for i in range(len(graph.adjacency_list[current])):
        edge_neighbour = graph.adjacency_list[current][i]
        if rec[edge_neighbour]:
            return True
        elif not visited[edge_neighbour]:
            if dfs(graph, visited, edge_neighbour, rec):
                return True

    rec[current] = False
    return False


def is_cyclic(graph):

    visited = [False for i in range(graph.getVertexCount())]
    rec = [False for i in range(graph.getVertexCount())]

    for i in range(graph.getVertexCount()):
        if not visited[i]:
            if dfs(graph, visited, i, rec):
                return True
    return False


if __name__ == '__main__':

    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(2, 3)
    graph.add_edge(2, 1)
    graph.add_edge(3, 4)
    graph.add_edge(4, 2)
    graph.add_edge(5, 2)
    graph.add_edge(5, 4)

    graph.display()

    print(is_cyclic(graph))
