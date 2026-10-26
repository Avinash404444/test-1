class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def display(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])


g = Graph()
for vertex in ['A', 'B', 'C', 'D']:
    g.add_vertex(vertex)

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

print("Graph using Adjacency List:")
g.display()
