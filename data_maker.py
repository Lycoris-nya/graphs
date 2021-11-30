import json
import sys
import time
import random

from graph_search_algorithms import GraphSearchAlgorithms, WeightedGraphSearchAlgorithms
from graph_builder import *


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
    for i in range(4, 700, 2):
        graph = GraphSearchAlgorithms(vertex_count=i, edges=get_random_graph(i, False))
        data[i] = measure(26, algorithm, graph, random.randint(0, i - 1), random.randint(0, i - 1))
    with open(name, "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))


def make_random_data_for_weighted_graph(name, algorithm):
    data = {}
    for i in range(4, 500, 2):
        graph = WeightedGraphSearchAlgorithms(vertex_count=i, edges=get_connected_graph_without_negative_edges(i, True))
        data[i] = measure(26, algorithm, graph)
    with open(name, "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))


def make_worst_data_for_weighted_graph(name, algorithm):
    data = {}
    for i in range(4, 500, 2):
        graph = WeightedGraphSearchAlgorithms(vertex_count=i, edges=get_dense_weighted_graph(i), oriented=True)
        data[i] = measure(26, algorithm, graph)
    with open(name, "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))


def make_best_data_for_weighted_graph(name, algorithm):
    data = {}
    for i in range(4, 500, 2):
        graph = WeightedGraphSearchAlgorithms(vertex_count=i, edges=get_weighted_chain(i), oriented=True)
        data[i] = measure(26, algorithm, graph)
    with open(name, "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))


def make_best_data(name, algorithm):
    data = {}
    for i in range(4, 700, 2):
        graph = GraphSearchAlgorithms(vertex_count=i, edges=get_chain(i))
        data[i] = measure(26, algorithm, graph, 0, i - 1)
    with open(name, "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))


def make_worst_data(name, algorithm):
    data = {}
    for i in range(4, 700, 2):
        graph = GraphSearchAlgorithms(vertex_count=i, edges=get_dense_graph(i), oriented=True)
        data[i] = measure(26, algorithm, graph, 0, i - 1)
    with open(name, "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    # make_random_data("dfs_random_data.json", GraphSearchAlgorithms.dfs)
    # make_random_data("bfs_random_data.json", GraphSearchAlgorithms.bfs)
    # make_best_data("dfs_best_data.json", GraphSearchAlgorithms.dfs)
    # make_best_data("bfs_best_data.json", GraphSearchAlgorithms.bfs)
    # make_worst_data("dfs_worst_data.json", GraphSearchAlgorithms.dfs)
    # make_worst_data("bfs_worst_data.json", GraphSearchAlgorithms.bfs)
    # make_best_data_for_weighted_graph("dijkstra_best_data.json", WeightedGraphSearchAlgorithms.dijkstra)
    # make_worst_data_for_weighted_graph("dijkstra_worst_data.json", WeightedGraphSearchAlgorithms.dijkstra)
    # make_random_data_for_weighted_graph("dijkstra_random_data.json", WeightedGraphSearchAlgorithms.dijkstra)
    make_random_data_for_weighted_graph("floyd_random_data.json", WeightedGraphSearchAlgorithms.floyd)
