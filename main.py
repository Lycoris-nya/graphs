from graph_search_algorithms import GraphSearchAlgorithms, WeightedGraphSearchAlgorithms
import os

os.environ["PATH"] += os.pathsep + 'D:/Graphviz/bin/'

if __name__ == '__main__':
    # g = GraphSearchAlgorithms(vertex_count=6, edges=[(0, 1), (0, 2), (2, 3), (2, 4), (4, 5), (3, 4)], oriented=False)
    # path_bfs1 = GraphSearchAlgorithms.bfs(g, 0, 5)
    # path_bfs1 = GraphSearchAlgorithms.bfs(g, 0, 5)
    # GraphSearchAlgorithms.show_graph(g, path_bfs1, '1')
    #
    # path_dfs1 = GraphSearchAlgorithms.dfs(g, 0, 5)
    # path_dfs1 = GraphSearchAlgorithms.dfs(g, 0, 5)
    # GraphSearchAlgorithms.show_graph(g, path_dfs1,'2')
    g = WeightedGraphSearchAlgorithms(vertex_count=6,
                                      edges=[(0, 1, 1), (0, 2, 2), (2, 3, 1), (2, 4, 10), (4, 5, 5), (3, 4, 1)],
                                      oriented=True)
    n, path = WeightedGraphSearchAlgorithms.dijkstra_with_path(g, 0, 5)
    print(path)
    WeightedGraphSearchAlgorithms.show_graph(g, path, '3')
