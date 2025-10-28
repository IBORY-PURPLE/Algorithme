import sys
from collections import defaultdict, deque

# --------------------------------------------------------------------
# 1. 그래프 클래스 및 위상 정렬 알고리즘 정의
# --------------------------------------------------------------------
class Graph:
    def __init__(self, n):
        """
        그래프를 초기화합니다.
        :param n: 노드의 개수
        """
        self.N = n
        self.G = defaultdict(list)
        self.In = defaultdict(int)

    def add_edge(self, s, e):
        """
        s에서 e로 가는 방향성 간선을 추가합니다.
        """
        self.G[s].append(e)
        self.In[e] += 1

    def topological_sort(self):
        """
        위상 정렬을 수행하고 결과를 리스트로 반환합니다.
        """
        result = []
        q = deque()

        # 진입 차수가 0인 노드를 큐에 삽입
        for i in range(1, self.N + 1):
            if self.In[i] == 0:
                q.append(i)

        # 큐가 빌 때까지 반복
        while q:
            v = q.popleft()
            result.append(v)

            # 해당 노드와 연결된 노드들의 진입 차수에서 1 빼기
            for i in self.G[v]:
                self.In[i] -= 1
                # 새롭게 진입 차수가 0이 된 노드를 큐에 삽입
                if self.In[i] == 0:
                    q.append(i)

        # 사이클 발생 여부 확인
        if len(result) != self.N:
            # 실제 코딩 테스트에서는 문제의 요구사항에 따라
            # 아무것도 출력하지 않거나 특정 메시지를 출력해야 할 수 있습니다.
            return None
        else:
            return result

# --------------------------------------------------------------------
# 2. 메인 실행 블록: 입력 처리 및 함수 호출
# --------------------------------------------------------------------
if __name__ == "__main__":

    # 코딩 테스트 시 빠른 입력을 위해 sys.stdin.readline을 사용합니다.
    # input()보다 훨씬 빠릅니다.
    input = sys.stdin.readline

    # 첫째 줄에서 노드의 개수(N)와 간선의 개수(M)를 입력받습니다.
    # "7 8" 같은 문자열을 입력받아 공백으로 나눈 후 정수로 변환합니다.
    N, M = map(int, input().strip().split())

    # 그래프 객체 생성
    my_graph = Graph(N)

    # M개의 줄에 걸쳐 간선 정보를 입력받습니다.
    for _ in range(M):
        s, e = map(int, input().strip().split())
        my_graph.add_edge(s, e)

    # 위상 정렬 수행
    sorted_result = my_graph.topological_sort()

    # 결과 출력
    if sorted_result:
        # 리스트의 원소들을 공백으로 구분하여 한 줄에 출력합니다.
        # 예: [1, 2, 3] -> "1 2 3"
        print(' '.join(map(str, sorted_result)))