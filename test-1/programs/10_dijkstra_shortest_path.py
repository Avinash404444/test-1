class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))

    def dijkstra(self, source):
        distance = {vertex: float('inf') for vertex in self.graph}
        distance[source] = 0
        visited = set()

        while len(visited) < len(self.graph):
            current = None
            minimum = float('inf')
            for vertex in self.graph:
                if vertex not in visited and distance[vertex] < minimum:
                    minimum = distance[vertex]
                    current = vertex
            if current is None:
                break
            visited.add(current)
            for neighbor, weight in self.graph[current]:
                new_distance = distance[current] + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
        return distance


g = Graph()
for vertex in ['A', 'B', 'C', 'D']:
    g.add_vertex(vertex)
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 8)

source = 'A'
result = g.dijkstra(source)
print("Shortest paths from", source)
for vertex in result:
    print(source, "->", vertex, "=", result[vertex])
