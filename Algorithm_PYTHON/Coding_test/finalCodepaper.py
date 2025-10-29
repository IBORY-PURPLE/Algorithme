import sys
import heapq
from collections import defaultdict, deque

INF = float('inf')
input = sys.stdin.readline

class Graph:
    def __init__(self, n):
        self.N = n
        # 벨만-포드, 크루스칼용 간선 리스트: [(출발, 도착, 가중치), ...]
        self.edges = []
        #위상정렬
        self.G = defaultdict(list)
        self.In = defaultdict(int)

    def add_edge(self, u, v, w):
        self.G[u].append(v)
        self.In[e] += 1
        self.edges.append((u,v,w))

    def bellman_ford(self, start):
        """
        - 시간 복잡도: O(VE)
        - 특징: 한 시작점에서 다른 모든 정점까지의 최단 경로 탐색
        - 장점: 음수 가중치가 있어도 사용 가능, 음수 사이클 판별 가능
        """
        dist = [INF] * (self.N + 1)
        dist[start] = 0

        # 최대 N-1(간선의 갯수)까지 간선을 사용해서 최단거리 구하고 N번째는
        # 음수 싸이클 확인용
        for i in range(self.N):
            for u, v, w in self.edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    if i == self.N - 1:
                        return None

        return dist

    def topological_sort(self):

        result = []
        q = deque()

        for i in range(1, self.N + 1):
            if self.In[i] == 0:
                q.append(i)

        while q:
            v = q.popleft()
            result.append(v)

            for i in self.G[v]:
                self.In[i] -= 1
                if self.In[i] == 0:
                    q.append(i)

        if len(result) != self.N:
            print("싸이클 발생")
            return None
        else:
            return result

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