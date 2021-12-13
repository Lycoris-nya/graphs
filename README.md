# graphs
Библиотека с алгоритмами на графах
```
    Реализует dfs, bfs, dijkstra, floyd
    Для создания графа в конструктор передается число вершин, список ребер, выставляются флаги
    Пример:
    GraphSearchAlgorithms(vertex_count=6, edges=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], oriented=False)
    WeightedGraphSearchAlgorithms(vertex_count=3, edges=[(0, 1, 1000), (1, 0, 5), (1, 2, 1)], oriented=True)
    
    Есть возможность физуальзировать путь в графе, для этого в метод show_graph нужно передать граф, путь, и имя графа
    
```
