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


def dijkstra(graph, source):

    distance = {key: float('inf') for key in graph.adjacency_list.keys()}
    visited = {key: False for key in graph.adjacency_list.keys()}

    distance[source] = 0
    queue = [(0, source)]

    while queue:
        current_distance, current = heapq.heappop(queue)
        if visited[current]:
            continue
        else:
            visited[current] = True
            for neighbour, weight in graph.adjacency_list[current]:
                new_distance = current_distance + weight
                if new_distance < distance[neighbour]:
                    distance[neighbour] = new_distance
                    heapq.heappush(queue, (distance[neighbour], neighbour))

    for vertex in distance:
        print(vertex, " -> ", distance[vertex])


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 7)
    graph.add_edge(2, 4, 3)
    graph.add_edge(3, 5, 1)
    graph.add_edge(4, 3, 2)
    graph.add_edge(4, 5, 5)
    graph.display()

    dijkstra(graph, 0)
