import sys
import heapq

# 다익스트라
while True:
    try:
        n, m, q, s = map(int, sys.stdin.readline().split())
    except (IOError, ValueError):
        break

    if n==0 and m==0 and q==0 and s==0:
        break

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))

    dist = [float('inf')] * n
    dist[s] = 0

    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))


    for _ in range(q):
        target = int(sys.stdin.readline())
        if dist[target] == float('inf'):
            print("Impossible")
        else:
            print(dist[target])

    print()


