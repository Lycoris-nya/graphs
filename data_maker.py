import json
import sys
import time
import random

from graph_search_algorithms import GraphSearchAlgorithms, WeightedGraphSearchAlgorithms
from graph_builder import get_random_graph


def measure(number_of_starts, algorithm, *args, **kwargs):
    for i in range(10):
        algorithm(*args, **kwargs)
    times = []

    for i in range(number_of_starts):
        start = time.perf_counter()
        algorithm(*args, **kwargs)
        time_delta = time.perf_counter() - start
        times.append(time_delta)
    return times


def make_random_data(name, algorithm):
    data = {}
    for i in range(4, 100, 2):
        graph = GraphSearchAlgorithms(vertex_count=i, edges=get_random_graph(i, False))
        data[i] = measure(26, algorithm, graph, random.randint(0, i - 1), random.randint(0, i - 1))
    with open(name, "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    make_random_data("dfs_random_data.json", GraphSearchAlgorithms.dfs)
    make_random_data("bfs_random_data.json", GraphSearchAlgorithms.bfs)
