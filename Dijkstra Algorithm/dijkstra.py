def dijkstra(start_node, graph):
    unvisited = {}
    visited = {}

    for node in graph:
        unvisited[node] = float('inf')

    current = start_node
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in graph[current].items():
            if neighbour not in unvisited:
                continue

            newDistance = currentDistance + distance
            if unvisited[neighbour] is float("inf") or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance

        visited[current] = currentDistance
        del unvisited[current]

        if not unvisited:
            break

        unvisited_items = [node for node in unvisited.items()]

        sorted_unvisited_items = sorted(unvisited_items, key=lambda x: x[1])
        current, currentDistance = sorted_unvisited_items[0]

    return visited


start_node = 'A'
graph = {
    'B': {'A': 5, 'D': 35, 'E': 10},
    'A': {'B': 5, 'C': 10},
    'D': {'B': 35, 'C': 20, 'E': 10},
    'C': {'A': 10, 'D': 20, 'E': 30},
    'E': {'B': 10, 'D': 10, 'C': 30}}

min_distances = dijkstra(start_node, graph)
print(min_distances)