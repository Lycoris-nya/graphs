import queue
from graphviz import Digraph
from graphviz import Source


class GraphSearchAlgorithms:

    def __init__(self, vertex_count=0, edges=[], oriented=False):
        self.vertex_count = vertex_count
        self.adjacent_vertices = []
        for i in range(vertex_count):
            self.adjacent_vertices.append(set())
        for edge in edges:
            self.adjacent_vertices[edge[0]].add(edge[1])
            if not oriented:
                self.adjacent_vertices[edge[1]].add(edge[0])

    def __int__(self, matrix=[]):
        self.vertex_count = len(matrix)
        self.adjacent_vertices = []
        for i in range(self.vertex_count):
            self.adjacent_vertices.append(set())
        for i in range(self.vertex_count):
            for j in range(self.vertex_count):
                self.adjacent_vertices[i].add(matrix[i][j])

    @staticmethod
    def restore_path(parents, start, end):
        path = list()
        if parents[end] == -1:
            return None
        while end != start:
            path.append(end)
            end = parents[end]
        path.append(start)
        path.reverse()
        return path

    @staticmethod
    def _dfs(graph, parents, previous, start, end):
        if previous == end:
            return True
        for current in graph.adjacent_vertices[previous]:
            if parents[current] == -1:
                parents[current] = previous
                if GraphSearchAlgorithms._dfs(graph, parents, current, start, end):
                    return True
        return False

    @staticmethod
    def dfs(graph, start, end):
        parents = [-1] * graph.vertex_count
        parents[start] = -2
        GraphSearchAlgorithms._dfs(graph, parents, start, start, end)
        return GraphSearchAlgorithms.restore_path(parents, start, end)

    @staticmethod
    def bfs(graph, start, end):
        vertex_queue = queue.Queue()
        vertex_queue.put(start)

        parents = [-1] * graph.vertex_count
        parents[start] = -2

        while not vertex_queue.empty():
            vertex = vertex_queue.get()
            if vertex == end:
                return GraphSearchAlgorithms.restore_path(parents, start, end)

            for next_vertex in graph.adjacent_vertices[vertex]:
                if parents[next_vertex] == -1:
                    parents[next_vertex] = vertex
                    vertex_queue.put(next_vertex)
        return None

    @staticmethod
    def show_graph(graph, path, name):
        graph_ = Digraph(name, comment='Graph')
        edges = set()
        for i in range(len(graph.adjacent_vertices)):
            graph_.node(str(i), str(i))
            for j in graph.adjacent_vertices[i]:
                edges.add((str(i), str(j)))
        for i in range(len(path) - 1):
            graph_.edge(str(path[i]), str(path[i + 1]), color='red')
            edges.remove((str(path[i]), str(path[i + 1])))
        for i in edges:
            graph_.edge(i[0], i[1])
        graph_.render(view=True)


class WeightedGraphSearchAlgorithms:

    def __init__(self, vertex_count=0, edges=[], oriented=False):
        self.negative_edge = False
        self.vertex_count = vertex_count
        self.adjacent_vertices = []
        for i in range(vertex_count):
            self.adjacent_vertices.append(set())
        for edge in edges:
            self.adjacent_vertices[edge[0]].add((edge[1], edge[2]))
            if not oriented:
                self.adjacent_vertices[edge[1]].add((edge[0], edge[2]))
            if edge[2] < 0:
                self.negative_edge = True

    def __int__(self, matrix=[]):
        self.negative_edge = False
        self.vertex_count = len(matrix)
        self.adjacent_vertices = []
        for i in range(self.vertex_count):
            self.adjacent_vertices.append(set())
        for i in range(self.vertex_count):
            for j in range(self.vertex_count):
                self.adjacent_vertices[i].add((matrix[i][j][0], matrix[i][j][1]))
                if matrix[i][j][1] < 0:
                    self.negative_edge = True

    @staticmethod
    def floyd(graph):
        res = [[float('inf') for _ in range(graph.vertex_count)] for _ in range(graph.vertex_count)]
        for i in range(graph.vertex_count):
            res[i][i] = 0
            for j in graph.adjacent_vertices[i]:
                res[i][j[0]] = j[1]
        for k in range(graph.vertex_count):
            for i in range(graph.vertex_count):
                for j in range(graph.vertex_count):
                    if res[i][k] != float('inf') and res[k][j] != float('inf') and res[i][j] > res[i][k] + res[k][j]:
                        res[i][j] = res[i][k] + res[k][j]
        return res

    @staticmethod
    def dijkstra(graph, start=0):
        if graph.negative_edge:
            return None
        matrix = [[float('inf') for _ in range(graph.vertex_count)] for _ in range(graph.vertex_count)]
        for i in range(graph.vertex_count):
            matrix[i][i] = 0
            for j in graph.adjacent_vertices[i]:
                matrix[i][j[0]] = j[1]
        min_dist = 0
        min_vertex = start

        distance = [float('inf')] * graph.vertex_count
        distance[start] = 0

        visited = [False] * graph.vertex_count

        while min_dist < float('inf'):
            i = min_vertex
            visited[i] = True
            for j in range(graph.vertex_count):
                if distance[i] + matrix[i][j] < distance[j]:
                    distance[j] = distance[i] + matrix[i][j]
            min_dist = float('inf')
            for j in range(graph.vertex_count):
                if not visited[j] and distance[j] < min_dist:
                    min_dist = distance[j]
                    min_vertex = j
        return distance

    @staticmethod
    def dijkstra_with_path(graph, start, end):
        if graph.negative_edge:
            return None
        parents = [-1] * graph.vertex_count
        parents[start] = -2
        distance = [float('inf')] * graph.vertex_count
        distance[start] = 0
        q = queue.PriorityQueue()
        q.put((0, start))
        while not q.empty():
            dist, vertex = q.get()
            if dist > distance[vertex]:
                continue
            if vertex == end:
                break
            for next in graph.adjacent_vertices[vertex]:
                if distance[next[0]] > distance[vertex] + next[1]:
                    parents[next[0]] = vertex
                    distance[next[0]] = distance[vertex] + next[1]
                    q.put((distance[next[0]], next[0]))
        return distance[end], GraphSearchAlgorithms.restore_path(parents, start, end)

    @staticmethod
    def show_graph(graph, path, name):
        graph_ = Digraph(name, comment='Graph')
        edges = set()
        for i in range(len(graph.adjacent_vertices)):
            graph_.node(str(i), str(i))
            for j in graph.adjacent_vertices[i]:
                edges.add((str(i), str(j[0]), str(j[1])))
        for i in range(len(path) - 1):
            min_edge = float('inf')
            for j in graph.adjacent_vertices[path[i]]:
                if j[0] == path[i + 1] and min_edge > j[1]:
                    min_edge = j[1]
            graph_.edge(str(path[i]), str(path[i + 1]), label=str(min_edge), color='red')
            edges.remove((str(path[i]), str(path[i + 1]), str(min_edge)))
        for i in edges:
            graph_.edge(i[0], i[1], label=i[2])
        graph_.render(view=True)
