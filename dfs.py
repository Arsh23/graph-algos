

class Graph():

    def __init__(self):
        self._graph = {}

    def add_node(self, name, edges):
        self._graph[name] = edges

    def display(self):
        print self._graph

    def dfs(self, start, item, visited=None, path=''):
        if start not in self._graph:
            raise Exception('Node not found in graph')
        if visited is None:
            visited = set()
        if path == '':
            path = str(start)
        else:
            path += '->' + str(start)

        visited.add(start)
        if start == item:
            print path
            return
        for x in self._graph[start]:
            if x not in visited:
                self.dfs(x, item, visited, path)


g = Graph()
g.add_node('a', ('b', 'd', 's'))
g.add_node('b', ('a', 'c', 's'))
g.add_node('c', ('b', 'e'))
g.add_node('d', ('a', 'g'))
g.add_node('e', ('c', 'g'))
g.add_node('g', ('d'))
g.add_node('s', ('a', 'b'))
# g.display()
g.dfs('s', 'g')
