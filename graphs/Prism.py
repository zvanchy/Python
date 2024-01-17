from collections import defaultdict
import heapq


class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, vertex1, vertex2, weight):
        self.adjacency_list[vertex1].append((vertex2, weight))
        self.adjacency_list[vertex2].append((vertex1, weight))

    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(vertex, " -> ", edges)


def prism(graph, startVertex):

    distances = {vertex: float('inf') for vertex in graph.adjacency_list}
    queue = [(0, 0)]
    distances[startVertex] = 0
    visited = {vertex: False for vertex in graph.adjacency_list}
    weighted_sum = 0

    while queue:
        current_distance, current = heapq.heappop(queue)
        if not visited[current]:
            visited[current] = True
            weighted_sum += current_distance
            for neighbour, weight in graph.adjacency_list[current]:
                if not visited[neighbour]:
                    heapq.heappush(queue,(weight, neighbour))

    print(weighted_sum)


graph = Graph()
graph.add_edge(0, 1, 10)
graph.add_edge(0, 2, 15)
graph.add_edge(0, 3, 30)
graph.add_edge(1, 3, 40)
graph.add_edge(2, 3, 50)
graph.display()
prism(graph, 0)
