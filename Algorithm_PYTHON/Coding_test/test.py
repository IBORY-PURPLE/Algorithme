import sys
import heapq

# 다익스트라 + 경로 복원
while True:
    try:
        n, m, q, s = map(int, sys.stdin.readline().split())
    except (IOError, ValueError):
        break

    if n == 0 and m == 0 and q == 0 and s == 0:
        break

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))

    INF = float('inf')
    dist = [INF] * n
    prev = [-1] * n               # 🔹 경로 복원용 부모 포인터
    dist[s] = 0

    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u       # 🔹 v의 최단 경로 상 직전 정점 기록
                heapq.heappush(pq, (nd, v))

    # 🔹 경로 복원 함수
    def restore_path(prev, s, t):
        if dist[t] == INF:
            return []             # 도달 불가
        path = []
        cur = t
        while cur != -1:
            path.append(cur)
            if cur == s:
                break
            cur = prev[cur]
        path.reverse()
        # 만약 prev[t]가 -1인데 t != s라면(이론상 dist[t]==INF이어야 함) 빈 경로 처리
        if not path or path[0] != s:
            return []
        return path

    for _ in range(q):
        target = int(sys.stdin.readline())
        if dist[target] == INF:
            print("Impossible")
        else:
            print(dist[target])
            path = restore_path(prev, s, target)
            # 경로 출력 형식: s -> ... -> target
            print("Path:", " -> ".join(map(str, path)))

    print()
