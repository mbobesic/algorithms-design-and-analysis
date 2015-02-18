__author__ = 'mislav'
from random import randint, choice


def load_graph():
    with open('assignment/kargerMinCut.txt') as f:

        lines = f.readlines()
        graph = {}

        i = 1
        for line in lines:

            i += 1
            neighbours = []
            unprocessed_neighbours = line.split()
            for index in xrange(1, len(unprocessed_neighbours)):
                neighbours.append(int(unprocessed_neighbours[index]))

            graph[int(unprocessed_neighbours[0])] = neighbours

    return graph


def karger_min_cut():
    graph = load_graph()
    while len(graph) > 2:
        a = choice(graph.keys())
        b = graph[a][randint(0, len(graph[a])-1)]
        for x in graph[a]:
            graph[x].remove(a)
            if x == b:
                continue
            graph[b].append(x)
            graph[x].append(b)

        graph.pop(a)

    a = choice(graph.keys())
    return len(graph[a])

result = []
for test_case_number in xrange(500):
    curr = karger_min_cut()
    result.append(curr)

print min(result)