from collections import defaultdict, deque

class Graph:
    def __init__(self, n):
        # 노드의 개수
        self.N = n
        # list()를 생성해서 해당 키값이 없어도 append가능하게 해주기.
        self.G = defaultdict(list)
        # 방문 여부를 확인할 리스트 (0으로 초기화)
        self.C = [0] * (n + 1)

    # 그래프에 간선을 추가하는 함수
    def add_edge(self, s, e):
        self.G[s].append(e)

    # 깊이 우선 탐색 (DFS)
    def dfs(self, v):
        # 현재 노드 방문 처리 및 출력
        print(v, end=" ")
        self.C[v] = 1

        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in self.G[v]:
            if not self.C[i]:
                self.dfs(i)

    # 너비 우선 탐색 (BFS)
    def bfs(self, s):
        # 큐(queue) 생성 및 시작 노드 삽입
        q = deque([s])
        # 시작 노드 방문 처리
        self.C[s] = 1

        while q:
            # 큐에서 하나의 원소를 뽑아 출력
            v = q.popleft()
            print(v, end=" ")

            # 해당 원소와 연결된, 아직 방문하지 않은 모든 원소들을 큐에 삽입
            for i in self.G[v]:
                if not self.C[i]:
                    q.append(i)
                    self.C[i] = 1

    # 방문 기록 초기화 함수
    def clear_visited(self):
        self.C = [0] * (self.N + 1)

# ----- 예제 사용법 -----
# 7개의 노드를 가진 그래프 생성 (1번부터 7번)
my_graph = Graph(7)

# 간선 추가
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(2, 5)
my_graph.add_edge(3, 6)
my_graph.add_edge(3, 7)

print("DFS 실행 결과:")
my_graph.dfs(1) # 1번 노드에서 DFS 시작
print("\n")

# 방문 기록 초기화
my_graph.clear_visited()

print("BFS 실행 결과:")
my_graph.bfs(1) # 1번 노드에서 BFS 시작
print("\n")