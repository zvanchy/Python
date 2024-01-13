class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = []

        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def get_neighbours(self, vertex):
        return self.adjacency_list[vertex]

    def getVertexCount(self):
        return len(self.adjacency_list)

    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(vertex, " -> ", edges)


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 5)
graph.add_edge(5, 6)

graph.display()


def dfs(graph, src, dest, visited, paths):
    if src == dest:
        print(paths + str(src))
        return

    for i in range(len(graph.get_neighbours(src))):

        if visited[graph.get_neighbours(src)[i]] == True:
            continue
        else:
            visited[src] = True
            dfs(graph, graph.get_neighbours(src)[
                i], dest, visited, paths + str(src))
            visited[graph.get_neighbours(src)[i]] = False


def findAllPaths(graph, src, dest, paths):
    if src == dest:
        return [[src]]
    visited = [False for i in range(graph.getVertexCount())]
    dfs(graph, src, dest, visited, paths)


src = 0
dest = 5
paths = ""
findAllPaths(graph, src, dest, paths)
