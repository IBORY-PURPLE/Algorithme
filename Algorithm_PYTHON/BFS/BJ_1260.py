from collections import deque
import sys

def dfs(start_node):
    visited_dfs[start_node] = True
    print(start_node, end=' ')

    for neighbor in graph[start_node]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

def bfs(start_node):
    queue = deque([start_node])
    visited_bfs[start_node] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for neighbor in graph[v]:
            if not visited_bfs[neighbor]:
                queue.append(neighbor)
                visited_bfs[neighbor] = True


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M, V = map(int, input().split())

    # N+1크기의 리스트 생성하는데 인덱스 0은 그럼 사용안함? ->사용한함. 인덱스 번호와 노드 번호를 일치시키기 위함
    # 2차원 리스트 만드는 구문 graph[1] = [] 빈 리스트를 추가해서 인접 노드 목록을 넣을 준비완료.
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N + 1):
        graph[i].sort()

    visited_dfs = [False] * (N + 1)
    visited_bfs = [False] * (N + 1)

    dfs(V)
    print()

    bfs(V)
    print()



