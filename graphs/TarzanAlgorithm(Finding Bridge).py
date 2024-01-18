

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

    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(vertex, " -> ", edges)


def dfs(graph, current, parent, visited, discoveryTime, lowestTime, time):

    visited[current] = True
    discoveryTime[current] = lowestTime[current] = time + 1

    for neighbour in graph.adjacency_list[current]:
        if neighbour == parent:
            continue
        elif not visited[neighbour]:
            dfs(graph, neighbour, current, visited,
                discoveryTime, lowestTime, time + 1)
            lowestTime[current] = min(
                lowestTime[current], lowestTime[neighbour])
            if discoveryTime[current] < lowestTime[neighbour]:
                print(f"Bride is {current} ---> {neighbour}")
        elif visited[neighbour]:
            lowestTime[current] = min(
                lowestTime[current], discoveryTime[neighbour])


def getBridge(graph):
    discoveryTime = {vertex: 0 for vertex in graph.adjacency_list}
    lowestTime = {vertex: 0 for vertex in graph.adjacency_list}
    visited = {vertex: False for vertex in graph.adjacency_list}
    time = 0
    for vertex in sorted(graph.adjacency_list):
        if not visited[vertex]:
            dfs(graph, vertex, -1, visited, discoveryTime, lowestTime, time)


graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 0)
graph.add_edge(2, 0)
graph.add_edge(0, 3)
graph.add_edge(3, 4)
# graph.add_edge(4, 5)
# graph.add_edge(3, 5)

graph.display()

getBridge(graph)
