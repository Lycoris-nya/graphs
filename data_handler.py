import json
from statistics import Statistics
import numpy as np

from matplotlib import pyplot as plt


def deserialization_data(path):
    res = dict()
    with open(path, 'r') as f:
        data = json.loads(f.read())
        for key in data.keys():
            res[key] = Statistics(len(data[key]), data[key])
    return res


def get_average(data):
    x = []
    y = []
    for key in data:
        x.append(int(key))
        y.append(data[key].average)
    return x, y


def make_chart(path):
    x, y = get_average(deserialization_data(path))
    plt.plot(x, y, "b.")
    plt.show()


def compare_charts(*paths):
    colour = {"r.", "b.", "g.", "c.", "m.", "y.", "k."}
    for path in paths:
        x, y = get_average(deserialization_data(path))
        plt.plot(x, y, colour.pop(), label=u"" + path)

    plt.legend()
    plt.show()


def linear_approximation(path):
    x, y = get_average(deserialization_data(path))
    b = np.zeros(shape=[len(x)])
    A = np.zeros(shape=[len(x), 2])
    for i in range(len(x)):
        b[i] = y[i]
        A[i][1] = 1
        A[i][0] = x[i]
    coefficients = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, b))
    y_approximation = []
    for i in range(len(x)):
        y_approximation.append(coefficients[0] * x[i] + coefficients[1])
    plt.plot(x, y, "r.", label=u"" + path)
    plt.plot(x, y_approximation)
    plt.legend()
    plt.show()


def square_approximation(path):
    x, y = get_average(deserialization_data(path))
    b = np.zeros(shape=[len(x)])
    A = np.zeros(shape=[len(x), 3])
    for i in range(len(x)):
        b[i] = y[i]
        A[i][2] = 1
        A[i][1] = x[i]
        A[i][0] = x[i] ** 2
    coefficients = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, b))
    y_approximation = []
    for i in range(len(x)):
        y_approximation.append(coefficients[0] * x[i] ** 2 + coefficients[1] * x[i] + coefficients[2])
    plt.plot(x, y, "r.", label=u"" + path)
    plt.plot(x, y_approximation)
    plt.legend()
    plt.show()


def cubic_approximation(path):
    x, y = get_average(deserialization_data(path))
    b = np.zeros(shape=[len(x)])
    A = np.zeros(shape=[len(x), 4])
    for i in range(len(x)):
        b[i] = y[i]
        A[i][3] = 1
        A[i][2] = x[i]
        A[i][1] = x[i] ** 2
        A[i][0] = x[i] ** 3
    coefficients = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, b))
    y_approximation = []
    for i in range(len(x)):
        y_approximation.append(
            coefficients[0] * x[i] ** 3 + coefficients[1] * x[i] ** 2 + coefficients[2] * x[i] + coefficients[3])
    plt.plot(x, y, "r.", label=u"" + path)
    plt.plot(x, y_approximation)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    linear_approximation("dfs_best_data.json")
    linear_approximation("bfs_best_data.json")
    square_approximation("dfs_worst_data.json")
    square_approximation("bfs_worst_data.json")
    square_approximation("dijkstra_worst_data.json")
    square_approximation("dijkstra_best_data.json")
    compare_charts("bfs_random_data.json", "dfs_random_data.json")
    compare_charts("bfs_best_data.json", "dfs_best_data.json")
    compare_charts("bfs_worst_data.json", "dfs_worst_data.json")
    compare_charts("bfs_worst_data.json", "bfs_random_data.json", "bfs_best_data.json")
    compare_charts("dfs_worst_data.json", "dfs_random_data.json", "dfs_best_data.json")
    compare_charts("dijkstra_worst_data.json", "dijkstra_random_data.json", "dijkstra_best_data.json")
    compare_charts("dijkstra_worst_data.json", "dijkstra_random_data.json", "dijkstra_best_data.json")
    cubic_approximation("floyd_random_data.json")
