import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def find_completion_time(N, G, task_times, order):
    dp_start = [0] * (N + 1)
    dp_finish  = [0] * (N + 1)

    for u in order:
        dp_finish[u] = dp_start[u] + task_times[u]

        for v in G[u]:
            dp_start[v] = max(dp_start[v], dp_finish[u])

    return max(dp_finish)

if __name__ == "__main__":
    N, M = map(int, input().split())

    task_times = [0] + list(map(int, input().split()))

    G = defaultdict(list)
    In = [0] * (N + 1)

    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        In[v] += 1