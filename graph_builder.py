import random


def get_random_graph(n, is_weighted, has_negative_edges=False):
    graph = set()
    for i in range(random.randint(0, min(100000, n ** 2 // 2))):
        if is_weighted:
            if has_negative_edges:
                graph.add((random.randint(0, n - 1), random.randint(0, n - 1), random.randint(-1000000000, 1000000000)))
            else:
                graph.add((random.randint(0, n - 1), random.randint(0, n - 1), random.randint(0, 1000000000)))
        else:
            graph.add((random.randint(0, n - 1), random.randint(0, n - 1)))
    return list(graph)


def get_tree_without_negative_edges(n, is_weighted):
    graph = set()
    order = [i for i in range(n)]
    random.shuffle(order)
    for i in range(1, n):
        if is_weighted:
            graph.add((order[random.randint(0, i - 1)], order[i], random.randint(0, 500000000)))
        else:
            graph.add((order[random.randint(0, i - 1)], order[i]))
    return list(graph)


def get_tree_with_negative_edges(n):
    graph = set()
    order = [i for i in range(n)]
    random.shuffle(order)
    for i in range(1, n):
        graph.add((order[random.randint(0, i - 1)], order[i], random.randint(-500000000, 500000000)))
    return list(graph)


def get_connected_graph_with_negative_edges(n):
    graph = get_tree_with_negative_edges(n)
    for i in range(random.randint(0, min(100000, n ** 2 // 2))):
        graph.append((random.randint(0, n - 1), random.randint(0, n - 1), random.randint(-500000000, 500000000)))
    return graph


def get_connected_graph_without_negative_edges(n, is_weighted):
    graph = get_tree_without_negative_edges(n, is_weighted)
    for i in range(random.randint(0, min(100500, n * (n - 1) // 2))):
        if is_weighted:
            graph.append((random.randint(0, n - 1), random.randint(0, n - 1), random.randint(0, 500000000)))
        else:
            graph.append((random.randint(0, n - 1), random.randint(0, n - 1)))
    return graph


def get_chain(n):
    graph = set()
    for i in range(n - 1):
        graph.add((i, i + 1))
    return list(graph)

def get_weighted_chain(n):
    graph = set()
    for i in range(n - 1):
        graph.add((i, i + 1,random.randint(0, 500000000)))
    return list(graph)


def get_dense_graph(n):
    graph = set()
    for i in range(n - 1):
        graph.add((i, i + 1))
    for i in range(n - 1):
        for j in range(i):
            graph.add((i, j))
    return list(graph)


def get_dense_weighted_graph(n):
    graph = set()
    for i in range(n - 1):
        graph.add((i, i + 1, random.randint(0, 500000000)))
    for i in range(n - 1):
        for j in range(i):
            graph.add((i, j, random.randint(0, 500000000)))
    return list(graph)
