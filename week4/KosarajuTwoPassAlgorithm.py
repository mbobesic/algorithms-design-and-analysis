__author__ = 'mislav'
import sys, resource

sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))


def load_graph():
    with open('assignment/SCC.txt') as f:

        global graph
        graph = {}
        for x in xrange(875714):
            graph[x+1] = []

        lines = f.readlines()

        for line in lines:

            pair = line.split()
            first = int(pair[0])
            second = int(pair[1])

            current = graph[first]
            current.append(second)
            graph[first] = current

    return graph


def reverse_graph():
    global graph, graph_rev

    for x in xrange(len(graph)):
        graph_rev[x+1] = []

    for first in graph.keys():
        for neighbour in graph[first]:
            current = graph_rev[neighbour]
            current.append(first)
            graph_rev[neighbour] = current

    graph = {}

visited = []
graph = {}
graph_rev = {}
order = []

def dfs(node):
    global visited, order

    visited[node] = True
    if node in graph:
        for neighbour in graph[node]:
            if visited[neighbour]:
                continue
            dfs(neighbour)

    order.append(node)


def kosaraju():
    global visited, graph, graph_rev
    graph = load_graph()

    visited = [False] * (len(graph) + 1)
    print "1"
    for node in graph.keys():
        if visited[node]:
            continue
        dfs(node)

    print "2"
    reverse_graph()

    visited = [False] * (len(graph_rev) + 1)
    result = [0] * (len(graph_rev)+1)

    print "3"
    for index in xrange(len(order), 0, -1):

        start_node = order[index-1]
        if visited[start_node]:
            continue

        stack = [start_node]
        while len(stack) > 0:
            current = stack.pop()
            if visited[current]:
                continue

            result[current] = start_node
            visited[current] = True

            for neighbour in graph_rev[current]:
                stack.append(neighbour)

    result.pop(0)
    total = {}
    for x in result:
        reps = total.get(x, 0)
        total[x] = reps + 1

    end_result = total.values()
    end_result.sort()
    end_result.reverse()

    while len(end_result) < 5:
        end_result.append(0)

    print end_result[0:5]

kosaraju()