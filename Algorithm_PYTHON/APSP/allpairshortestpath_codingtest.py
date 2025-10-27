import sys

while True:
    try:
        n, m, q = map(int, sys.stdin.readline().split())
    except (IOError, ValueError):
        break

    if n == 0 and m == 0 and q == 0:
        break

    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        dist[u][v] = min(dist[u][v], w)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf') and dist[k][k] < 0:
                    dist[i][j] = -float('inf')

    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())

        if dist[u][v] == float('inf'):
            print("Impossible")
        elif dist[u][v] == -float('inf'):
            print("-Infinity")
        else:
            print(dist[u][v])

    print()