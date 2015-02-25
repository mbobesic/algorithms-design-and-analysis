__author__ = 'mislav'


wanted_distances = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

inf = 2000000


def load_graph():
    with open('assignment/dijkstraData.txt') as f:

        global graph
        graph = {}

        lines = f.readlines()

        for line in lines:

            pair = line.split()
            first = int(pair[0])

            current = {}
            for index in xrange(1,len(pair)):
                edge = pair[index].split(',')
                current[int(edge[0])] = int(edge[1])

            graph[first] = current
    return graph


def get_result(result):
    return min(result, 1000000)


def dijkstra():
    current_graph = load_graph()

    not_visited = {x for x in current_graph.keys()}
    distance = {x: 2000000 for x in current_graph.keys()}

    distance[1] = 0

    while len(not_visited) > 0:
        node = -1
        current_distance = inf + 1
        for x in not_visited:
            if distance[x] < current_distance:
                node = x
                current_distance = distance[x]

        not_visited.remove(node)
        for neighbour in current_graph[node].keys():

            length = current_graph[node][neighbour]
            if distance[neighbour] > current_distance + length:
                distance[neighbour] = current_distance + length

    return distance

results = dijkstra()
output = ""
for x in wanted_distances:

    output = output + str(results[x]) + ","

print output

