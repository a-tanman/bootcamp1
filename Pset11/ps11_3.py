class Vertex:
    
    def __init__(self, key):
        self.key = key
        self.connected_to = dict()

    def add_neighbour(self, vertex, weight = 0):
        
        self.connected_to.update({vertex : weight})

    def get_connections(self):
        return self.connected_to

    def get_key(self):
        return self.key

    def get_weight(self, neighbour_v):
        return self.connected_to[neighbour_v]

    def __str__(self):
        if len(self.connected_to) > 0:
            return 'Vertex {} is connected to {}'.format(self.key, *[(str(b) + ',') for b in self.connected_to.keys()])
    
class VertexSearch(Vertex):

    def init(self, key, distance = 0, predescessor = None, color = 'white'):
        self.distance = distance
        self.predescessor = predescessor
        self.color = color
        super().__init__(key)

    def set_distance(self, distance):
        self.distance = distance

    def set_predescessor(self, predescessor):
        self.predescessor  = predescessor

    def set_color(self, color):
        self.color = color
    
    def get_distance(self):
        return self.distance

    def get_predescessor(self):
        return self.predescessor

    def get_color(self):
        return self.color

    def __lt__(self, other):
        if self.get_key() < other.get_key():
            return True
        else:
            return False
    
class Graph:
    
    def __init__(self):
        self.vertices = []
        self.num_vertices = 0

    def add_vertex(self, key):
        vertex = Vertex(key)
        self.vertices.append(vertex)
        self.num_vertices += 1

    def add_edge(self, from_v, to_v, weight = 0):
        self.get_vertex(from_v).add_neighbour(to_v, weight)

    def get_vertex(self, key):
        for v in self.vertices:
            if v.get_key() == key:
                return v
            
    def __contains__(self, key):
        return bool(self.get_vertex(key))

    def __iter__(self):
        for item in self.vertices:
            yield item

class GraphSearch(Graph):

    def __init__(self):
        super().__init__()

    def add_vertex(self, key):
        vertex = VertexSearch(key)
        self.vertices.append(vertex)
        self.num_vertices += 1

class GraphSearchUndirected(GraphSearch):
    def __init__(self):
        super().__init__()

    def add_edge(self, v1, v2, weight = 0):
        self.get_vertex(v1).add_neighbour(v2, weight)
        self.get_vertex(v2).add_neighbour(v1, weight)

import pickle

def build_graph(word_list):
    g = GraphSearch()
    for word in word_list:
        g.add_vertex(word.upper())

    return g


# This is to load the list of words
with open("C:/Users/Andrew Tan/development/python_course/solutions_andrew_tan/Pset11/words_list.pickle","rb") as f:
	words = pickle.load(f)

# this is to generate the graph
g = build_graph(words)

# print(words)
# This is to store the graph into another pickle object
import sys
sys.setrecursionlimit(0x100000)
with open("C:/Users/Andrew Tan/development/python_course/solutions_andrew_tan/Pset11/graph.pickle", "wb") as f:
	pickle.dump(g, f)

g.get_vertex('ZYTHUM')


# g = Graph()
# g.add_vertex(1)
# g.add_vertex(2)
# g.add_vertex(3)
# g.add_vertex(4)

# g.add_edge(1,2)
# g.add_edge(2,1, 5)

# g = GraphSearchUndirected()
# g.add_vertex(1)
# g.add_vertex(2)
# g.add_edge(1,2)
# print(g.get_vertex(2))