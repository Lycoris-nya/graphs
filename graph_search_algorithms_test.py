import unittest
from graph_search_algorithms import GraphSearchAlgorithms, WeightedGraphSearchAlgorithms


class MyTestCase(unittest.TestCase):
    def test_undirected_graph(self):
        g = GraphSearchAlgorithms(vertex_count=6, edges={(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)}, oriented=False)
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
        g = GraphSearchAlgorithms(vertex_count=6, edges={(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)}, oriented=True)
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

    def test1(self):
        g = WeightedGraphSearchAlgorithms(vertex_count=3, edges=[(0, 1, 3), (0, 2, 1), (2, 1, 1)], oriented=True)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g)[0][0], 0)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g)[0][1], 2)
        self.assertEqual(WeightedGraphSearchAlgorithms.floyd(g)[0][2], 1)
        self.assertEqual(WeightedGraphSearchAlgorithms.dijkstra(g, 0)[1], 2)
        self.assertEqual(WeightedGraphSearchAlgorithms.dijkstra(g, 0)[2], 1)


if __name__ == '__main__':
    unittest.main()
