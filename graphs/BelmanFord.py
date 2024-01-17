"""
Bellman Ford Algorith for negative and positive weighted 

"""
from collections import defaultdict


class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, vertex1, vertex2, weight):
        self.adjacency_list[vertex1].append((vertex2, weight))
        # self.adjacency_list[vertex2].append((vertex1, weight))

    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(vertex, " -> ", edges)


def bellmanFord(graph, startVertex):
    distance = {vertex: float('inf') for vertex in graph.adjacency_list}
    distance[startVertex] = 0

    # Belman ford ensures that it will find the path within v-1 nodes in v graph..which is
    # maximum number of nodes required to get the path

    for _ in range(len(graph.adjacency_list)-1):
        for vertex in graph.adjacency_list:
            for neighbour, weight in graph.adjacency_list[vertex]:
                if distance[vertex] != float('inf') and distance[vertex] + weight < distance[neighbour]:
                    distance[neighbour] = distance[vertex] + weight

    # Check for negative weight cycles
    # if the weight is again being updated that means it contains a negative cycle
    # and the values keeps increasing in negative
    for vertex in graph.adjacency_list:
        for neighbor, weight in graph.adjacency_list[vertex]:
            if distance[vertex] != float('inf') and distance[vertex] + weight < distance[neighbor]:
                print("Graph contains negative weight cycle")
                return

    for vertex in distance:
        print(vertex, " -> ", distance[vertex])


graph = Graph()
graph.add_edge(0, 1, 2)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, -4)
graph.add_edge(2, 3, 2)
graph.add_edge(3, 4, 4)
graph.add_edge(4, 1, -1)
graph.display()
bellmanFord(graph, 0)
