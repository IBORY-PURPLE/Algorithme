from collections import deque
import sys

input = sys.stdin.readline

INF = 10**9

def bfs(s, t, parent, adj, capacity):
    for i in range(len(parent)):
        parent[i] = -1
    parent[s] = -2
    q = deque([(s, INF)])

    while q:
        cur, flow = q.popleft()

        for nxt in adj[cur]:
            if parent[nxt] == -1 and capacity[cur][nxt] > 0:
                parent[nxt] = cur
                new_flow = min(flow, capacity[cur][nxt])
                if nxt == t:
                    return new_flow
                q.append((nxt, new_flow))

    return 0

def edmonds_karp(n, adj, capacity, s, t):
    flow = 0
    parent = [-1] * n

    while True:
        new_flow = bfs(s, t, parent, adj, capacity)
        if new_flow == 0:
            break

        flow += new_flow
        v = t
        while v != s:
            u = parent[v]
            capacity[u][v] -= new_flow
            capacity[v][u] += new_flow
            v = u

    return flow

def char_to_index(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a') + 26


if __name__ == "__main__":
    """
    adj = [
  [],  # 0번 노드의 인접노드 목록
  [],  # 1번 노드의 인접노드 목록
  [],  # 2번 노드의 인접노드 목록
  []   # 3번 노드의 인접노드 목록
]
    """
    n = int(input())
    adj = [[] for _ in range(52)]

    capacity = [[0] * 52 for _ in range(52)]

    for _ in range(n):
        a, b, c = input().split()
        u = char_to_index(a)
        v = char_to_index(b)
        c = int(c)

        adj[u].append(v)
        adj[v].append(u)
        capacity[u][v] += c
        capacity[v][u] += c

    s = char_to_index('A')
    t = char_to_index('Z')

    print(edmonds_karp(52, adj, capacity, s, t))

