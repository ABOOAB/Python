import random

"""define the vertex ,every vertex will have a value(word) and
a dictionary which contain the other vertices and it's weigh(edge)"""

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjecent = {} # neighbor vertex and its weight
        self.neighbors = [] # all neighbor vertices (words)
        self.neighbors_weights = [] # all neighbour weights (edges)


    # add new vertex
    def add_edge_to (self, vertex, weight = 0):
        self.adjecent[vertex] = weight

    # increase the wieght of an exist vertex
    def increment_edge (self, vertex):
        self.adjecent[vertex] = self.adjecent.get(vertex, 0) + 1

    # probability map
    def get_probability_map(self):
        for(vertex, weight) in self.adjecent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    # get the next word
    def next_word(self):
        return random.choices(self.neighbors, weights = self.neighbors_weights)[0]



class Graph:
    def __init__(self) :
        self.vertices = {} # word: Vertex(word)

    def get_vertex_value(self):
        return set(self.vertices.keys())
    
    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)

        return self.vertices[value]
    
    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()