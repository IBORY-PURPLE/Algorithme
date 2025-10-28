# ======================================================================
# 코딩 테스트용 최단 경로 알고리즘 템플릿 (Python)
# 1. 다익스트라 (Dijkstra)
# 2. 벨만-포드 (Bellman-Ford)
# 3. 플로이드-워셜 (Floyd-Warshall)
# ======================================================================

import sys
import heapq
from collections import defaultdict

# 무한대를 의미하는 값으로, 실제 간선 가중치의 합보다 충분히 큰 값 사용
INF = float('inf')

# ----------------------------------------------------------------------
# 그래프 클래스 정의
# ----------------------------------------------------------------------
class Graph:
    def __init__(self, n):
        self.N = n  # 노드의 개수
        # 다익스트라용 인접 리스트: {노드: [(연결된 노드, 가중치), ...]}
        self.adj = defaultdict(list)
        # 벨만-포드, 크루스칼용 간선 리스트: [(출발, 도착, 가중치), ...]
        self.edges = []
        # 플로이드-워셜용 인접 행렬
        self.dist_matrix = [[INF] * (n + 1) for _ in range(n + 1)]

    def add_edge(self, u, v, w):
        """간선 추가 (다익스트라, 벨만-포드용)"""
        self.adj[u].append((v, w))
        self.edges.append((u, v, w))

    # ------------------------------------------------------------------
    # 2.4 최단 거리 - 다익스트라 (Dijkstra)
    # - 시간 복잡도: O(E log V) (E: 간선 수, V: 노드 수)
    # - 특징: 한 시작점에서 다른 모든 정점까지의 최단 경로 탐색
    # - 제약: 간선의 가중치는 반드시 0 이상이어야 함 (음수 가중치 X)
    # ------------------------------------------------------------------
    def dijkstra(self, start):
        dist = [INF] * (self.N + 1)
        dist[start] = 0
        pq = [(0, start)]  # (거리, 노드) 우선순위 큐

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return dist

    # ------------------------------------------------------------------
    # 2.5 최단 거리 - 벨만-포드 (Bellman-Ford)
    # - 시간 복잡도: O(VE)
    # - 특징: 한 시작점에서 다른 모든 정점까지의 최단 경로 탐색
    # - 장점: 음수 가중치가 있어도 사용 가능, 음수 사이클 판별 가능
    # ------------------------------------------------------------------
    def bellman_ford(self, start):
        dist = [INF] * (self.N + 1)
        dist[start] = 0

        # N-1번 동안 모든 간선에 대해 완화(relaxation) 작업 반복
        for i in range(self.N):
            for u, v, w in self.edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    # N번째 반복에서도 갱신이 발생하면 음수 사이클 존재
                    if i == self.N - 1:
                        return None  # 음수 사이클 존재

        return dist

    # ------------------------------------------------------------------
    # 2.3 최단 거리 - 플로이드-워셜 (Floyd-Warshall)
    # - 시간 복잡도: O(V^3)
    # - 특징: 모든 정점에서 모든 다른 정점까지의 최단 경로 탐색
    # - 장점: 코드가 매우 간결함. 음수 가중치도 처리 가능 (음수 사이클은 X)
    # ------------------------------------------------------------------
    def run_floyd_warshall(self):
        # dist_matrix는 main에서 직접 초기화
        dist = self.dist_matrix

        for k in range(1, self.N + 1):  # 경유지
            for i in range(1, self.N + 1):  # 출발지
                for j in range(1, self.N + 1):  # 도착지
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist

# ======================================================================
# 메인 실행 블록: 입력 처리 및 함수 호출
# ======================================================================
if __name__ == "__main__":
    input = sys.stdin.readline

    # --- 다익스트라 (Dijkstra) 예제 ---
    print("--- 1. Dijkstra ---")
    # 입력 형식:
    # N(노드 수) M(간선 수)
    # start_node(시작 노드)
    # M개의 줄에 u v w (u->v, 가중치 w)
    N, M = map(int, input().strip().split())
    start_node = int(input().strip())
    graph_dijkstra = Graph(N)
    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        graph_dijkstra.add_edge(u, v, w)

    distances = graph_dijkstra.dijkstra(start_node)
    for i in range(1, N + 1):
        print(f"Node {i}: {distances[i] if distances[i] != INF else 'INF'}")
    print("-" * 20)

    # --- 벨만-포드 (Bellman-Ford) 예제 ---
    print("--- 2. Bellman-Ford ---")
    # 입력 형식: 다익스트라와 동일
    N, M = map(int, input().strip().split())
    start_node = int(input().strip())
    graph_bellman = Graph(N)
    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        graph_bellman.add_edge(u, v, w)

    distances = graph_bellman.bellman_ford(start_node)
    if distances is None:
        print("음수 사이클이 존재합니다.")
    else:
        for i in range(1, N + 1):
            print(f"Node {i}: {distances[i] if distances[i] != INF else 'INF'}")
    print("-" * 20)

    # --- 플로이드-워셜 (Floyd-Warshall) 예제 ---
    print("--- 3. Floyd-Warshall ---")
    # 입력 형식:
    # N(노드 수)
    # M(간선 수)
    # M개의 줄에 u v w (u->v, 가중치 w)
    N = int(input().strip())
    M = int(input().strip())
    graph_floyd = Graph(N)
    dist = graph_floyd.dist_matrix

    for i in range(1, N + 1):
        dist[i][i] = 0 # 자기 자신으로 가는 비용은 0

    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        dist[u][v] = min(dist[u][v], w) # 여러 간선이 있을 수 있으므로 최소값 저장

    all_distances = graph_floyd.run_floyd_warshall()
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            val = all_distances[i][j]
            print(val if val != INF else "INF", end=" ")
        print()
    print("-" * 20)