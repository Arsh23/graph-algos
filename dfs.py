

class Graph():

    def __init__(self):
        self._graph = {}

    def add_node(self, name, edges):
        self._graph[name] = edges

    def display(self):
        print self._graph

    # def dfs_stack(graph, start):
    #     pass

g = Graph()
g.add_node('a', ('b', 'd', 's'))
g.add_node('b', ('a', 'c', 's'))
g.add_node('c', ('b', 'e'))
g.add_node('d', ('a', 'g'))
g.add_node('e', ('c'))
g.add_node('g', ('d'))
g.add_node('s', ('a', 'b'))
g.display()
