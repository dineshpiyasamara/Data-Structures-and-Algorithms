def bellman_ford(start_node, graph):
    distance = {}

    for node in graph:
        distance[node] = float('inf')

    current_distance = 0
    distance[start_node] = current_distance

    for i in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour] = distance[node] + \
                        graph[node][neighbour]

    for node in graph:
        for neighbour in graph[node]:
            if (distance[neighbour] > distance[node] + graph[node][neighbour]):
                return "There is a Negative weight cycle"

    return distance

start_node = 'A'
graph = {
    'A': {'B': 3, 'C':  5},
    'B': {'C': 3},
    'C': {'D': 4},
    'D': {'B': -2}}

distance = bellman_ford(start_node, graph)
print(distance)
