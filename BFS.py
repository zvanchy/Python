from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append((vertex2))
        # self.adjacency_list[vertex2].append(vertex1)

    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(vertex, " -> ", edges)


graph = Graph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 0)
graph.add_edge(1, 3)
graph.add_edge(2, 0)
graph.add_edge(2, 4)
graph.add_edge(3, 1)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 2)
graph.add_edge(4, 3)
graph.add_edge(4, 5)
graph.add_edge(5, 3)
graph.add_edge(5, 4)
graph.add_edge(5, 6)
graph.add_edge(6, 5)

graph.display()
print(graph.adjacency_list)


def bfs(vertexCount):
    queue = deque()
    visited = [False for i in range(vertexCount+1)]
    queue.append(0)
    while (queue):
        s = (int)(queue.popleft())
        if visited[s] == True:
            continue
        else:
            print(s)
            visited[s] = True
            neighbours = graph.adjacency_list[s]
            for i in range(len(neighbours)):
                queue.append(neighbours[i])


def dfs(graph, current, visitedArray):
    print(current, end=" ")
    visitedArray[int(current)] = 1
    for i in range(len(graph.adjacency_list[current])):
        if visitedArray[graph.adjacency_list[current][i]] == False:
            dfs(graph, graph.adjacency_list[current][i], visitedArray)


bfs(6)

visited_array = [False for i in range(7)]
dfs(graph, 0, visited_array)
