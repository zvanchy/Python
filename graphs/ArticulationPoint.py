class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = []

        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def display(self):
        for vertex, edge in self.adjacency_list.items():
            print(f"{vertex} -> {edge}")


def articulationPoint(graph):
    visited = {vertex: False for vertex in graph.adjacency_list}
    parent = -1
    current = 0
    discoveryTime = {vertex: float('inf') for vertex in graph.adjacency_list}
    lowestTime = {vertex: float('inf') for vertex in graph.adjacency_list}
    time = 0
    children = 0
    for vertex in graph.adjacency_list.keys():
        if not visited[vertex]:
            dfs(graph, current, parent, visited, time,
                discoveryTime, lowestTime, children)


def dfs(graph, current, parent, visited, time, discoveryTime, lowestTime, children):

    visited[current] = True
    discoveryTime[current] = lowestTime[current] = time + 1

    for neighbour in graph.adjacency_list[current]:
        if neighbour == parent:
            continue
        elif not visited[neighbour]:
            dfs(graph, neighbour, current, visited, time +
                1, discoveryTime, lowestTime, children)
            lowestTime[current] = min(
                lowestTime[current], lowestTime[neighbour])

            # check for articulation point
            if discoveryTime[current] <= lowestTime[neighbour] and parent != -1:
                print(f"Articulation point: {current}")

            children += 1
        elif visited[neighbour]:
            lowestTime[current] = min(
                lowestTime[current], discoveryTime[neighbour])
            
    if parent == -1 and children > 1 :
       print(f"Articulation point: {current}")
 
    pass


graph = Graph()


graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(0, 3)
graph.add_edge(3, 4)
graph.display()

articulationPoint(graph)
