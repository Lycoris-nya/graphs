import unittest

import graph_builder
from graph_search_algorithms import GraphSearchAlgorithms, WeightedGraphSearchAlgorithms
import queue
from graph_builder import *


class MyTestCase(unittest.TestCase):
    def test_undirected_graph(self):
        g = GraphSearchAlgorithms(vertex_count=6, edges=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], oriented=False)
        path_dfs1 = GraphSearchAlgorithms.dfs(g, 0, 5)
        path_bfs1 = GraphSearchAlgorithms.bfs(g, 0, 5)
        path_dfs2 = GraphSearchAlgorithms.dfs(g, 2, 5)
        path_bfs2 = GraphSearchAlgorithms.bfs(g, 2, 5)
        path_dfs3 = GraphSearchAlgorithms.dfs(g, 2, 1)
        path_bfs3 = GraphSearchAlgorithms.bfs(g, 2, 1)
        path_dfs4 = GraphSearchAlgorithms.dfs(g, 1, 1)
        path_bfs4 = GraphSearchAlgorithms.bfs(g, 1, 1)
        self.assertEqual(path_dfs1, [0, 1, 2, 3, 4, 5])
        self.assertEqual(path_bfs1, [0, 1, 2, 3, 4, 5])
        self.assertEqual(path_dfs2, [2, 3, 4, 5])
        self.assertEqual(path_bfs2, [2, 3, 4, 5])
        self.assertEqual(path_dfs3, [2, 1])
        self.assertEqual(path_bfs3, [2, 1])
        self.assertEqual(path_dfs4, [1])
        self.assertEqual(path_bfs4, [1])

    def test_directed_graph(self):
        g = GraphSearchAlgorithms(vertex_count=6, edges=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], oriented=True)
        path_dfs1 = GraphSearchAlgorithms.dfs(g, 0, 5)
        path_bfs1 = GraphSearchAlgorithms.bfs(g, 0, 5)
        path_dfs2 = GraphSearchAlgorithms.dfs(g, 5, 2)
        path_bfs2 = GraphSearchAlgorithms.bfs(g, 5, 2)
        path_dfs3 = GraphSearchAlgorithms.dfs(g, 2, 1)
        path_bfs3 = GraphSearchAlgorithms.bfs(g, 2, 1)
        path_dfs4 = GraphSearchAlgorithms.dfs(g, 1, 1)
        path_bfs4 = GraphSearchAlgorithms.bfs(g, 1, 1)
        self.assertEqual(path_dfs1, [0, 1, 2, 3, 4, 5])
        self.assertEqual(path_bfs1, [0, 1, 2, 3, 4, 5])
        self.assertEqual(path_dfs2, None)
        self.assertEqual(path_bfs2, None)
        self.assertEqual(path_dfs3, None)
        self.assertEqual(path_bfs3, None)
        self.assertEqual(path_dfs4, [1])
        self.assertEqual(path_bfs4, [1])

    def test_dijkstra_not_work_with_negative_weight(self):
        g = WeightedGraphSearchAlgorithms(vertex_count=3, edges=[(0, 2, -2), (0, 1, -1), (2, 1, 1)], oriented=True)
        self.assertEqual(WeightedGraphSearchAlgorithms.dijkstra(g, 0), None)

    def test_floyd_work_with_negative_weight(self):
        g = WeightedGraphSearchAlgorithms(vertex_count=4, edges=[(0, 1, -10), (0, 2, 9), (2, 3, -1)], oriented=True)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g)[0][1], -10)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g)[0][2], 9)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g)[0][3], 8)



    def test_weighted_graph_search_algorithms(self):
        g1 = WeightedGraphSearchAlgorithms(vertex_count=3, edges=[(0, 2, 1), (0, 1, 5), (2, 1, 1)], oriented=True)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g1)[0][0], 0)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g1)[0][1], 2)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g1)[0][2], 1)
        self.assertEqual(WeightedGraphSearchAlgorithms.dijkstra(g1, 0)[1], 2)
        self.assertEqual(WeightedGraphSearchAlgorithms.dijkstra(g1, 0)[2], 1)

        g2 = WeightedGraphSearchAlgorithms(vertex_count=3, edges=[(0, 1, 1000), (1, 0, 5), (1, 2, 1)], oriented=False)
        self.assertEqual(WeightedGraphSearchAlgorithms.dijkstra(g2, 0)[1], 5)
        self.assertEqual(WeightedGraphSearchAlgorithms.dijkstra(g2, 0)[2], 6)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g2)[0][1], 5)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g2)[0][2], 6)

        g3 = WeightedGraphSearchAlgorithms(vertex_count=3, edges=[(0, 1, 1000), (1, 0, 5), (1, 2, 1)], oriented=True)
        self.assertEqual(WeightedGraphSearchAlgorithms.dijkstra(g3, 0)[1], 1000)
        self.assertEqual(WeightedGraphSearchAlgorithms.dijkstra(g3, 0)[2], 1001)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g3)[0][1], 1000)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g3)[0][2], 1001)


    def is_graph_connected(self, vertex_count, edges):
        q = queue.Queue()
        adjacent_vertices = []
        for visit in range(vertex_count):
            adjacent_vertices.append(set())
        for visit in edges:
            adjacent_vertices[visit[0]].add(visit[1])
            adjacent_vertices[visit[1]].add(visit[0])
        visited = [False] * vertex_count
        q.put(0)
        visited[0] = True
        while not q.empty():
            vertex = q.get()
            for neighbour in adjacent_vertices[vertex]:
                if not visited[neighbour]:
                    q.put(neighbour)
                    visited[neighbour] = True
        for visit in visited:
            if not visit:
                return False
        return True

    def test_tree_builder(self):
        for i in range(1, 100):
            graphs = []
            graphs.append(graph_builder.get_tree_without_negative_edges(i * 2, False))
            graphs.append(graph_builder.get_tree_without_negative_edges(i * 2, True))
            graphs.append(graph_builder.get_tree_with_negative_edges(i * 2))
            for j in graphs:
                self.assertEqual(len(j), i*2-1)
                self.assertEqual(self.is_graph_connected(i * 2, j), True)


if __name__ == '__main__':
    unittest.main()
