INF = 9999

graph = [[0, 6, 2, INF],
         [INF, 0, INF, 1],
         [INF, 3, 0, 7],
         [4, INF, INF, 0]]


def printMatrix(graph, numVertices):
    for i in range(numVertices):
        for j in range(numVertices):
            if (graph[i][j] == INF):
                print("INF", end="  ")
            else:
                print(graph[i][j], end="  ")
        print("  ")


def floydWarshall(graph, numVertices):
    for k in range(numVertices):
        print()
        for i in range(numVertices):
            for j in range(numVertices):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
        printMatrix(graph, numVertices)


floydWarshall(graph, len(graph))
