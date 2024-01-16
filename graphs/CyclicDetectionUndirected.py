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
        for vertex, edge in self.adjacency_list.items():
            print(vertex, " -> ", edge)

    def get_neighbour_count(self, vertex):
        return len(self.adjacency_list[vertex])

    def get_neighbours(self, vertex):
        return self.adjacency_list[vertex]


def cycleDetection(graph, visited, current, parent):

    visited[current] = True

    for neighbour in graph.get_neighbours(current):

        '''in graph 0-----1---3
                     \   /
                       2   

             for neighbour of 1 that is 2...
                0 is already visited but parent of 2 is not 0... 0 is fetched as neighbour in code       
                this is the cyclic condition
        '''
        if visited[neighbour] and not parent == neighbour:
            return True

        if not visited[neighbour] and not parent == current:
            if cycleDetection(graph, visited, neighbour, current):
                return True

    return False


def is_cyclic(graph):
    for i in graph.adjacency_list.keys():
        visited = {key: False for key in graph.adjacency_list.keys()}
        if cycleDetection(graph, visited, i, -1):
            return True

    return False


if __name__ == '__main__':
    graph = Graph()

    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)
    graph.add_edge(2, 4)
    # graph.add_edge(2, 3)
    # graph.add_edge(2, 4)
    # graph.add_edge(3, 5)
    # graph.add_edge(4, 5)

    graph.display()

    print(is_cyclic(graph))
