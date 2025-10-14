from collections import deque

def kahn_topological_sort(graph):
    """
    칸의 알고리즘(Kahn's Algorithm)을 사용하여 위상 정렬(Topological Sort)을 수행합니다.

    Args:
        graph (dict): 인접 리스트 형태로 표현된 방향 그래프.
                      예: {'A': ['B', 'C'], ...}

    Returns:
        list or str: 위상 정렬된 정점 리스트를 반환합니다.
                     만약 그래프에 사이클이 존재하면, 경고 메시지 문자열을 반환합니다.
    """
    # in_degrees 딕셔너리로 정점마다의 진입차수 구하기
    in_degrees = {u: 0 for u in graph}
    # 그래프에 등장하는 모든 정점을 포함하기 위해 목적지 정점도 추가
    # F정점이 나가는 간선이 없어서 그래프에 명시적으로 작성을 하지 않는다면 위 indegree초기화에서
    # 적용이 안되기 때문에 해주는 것인데 지금 이 코드에서 'F': []로 명시해줬기 때문에 상관 없음. 지워도 됨.
    for u in graph:
        for v in graph[u]:
            if v not in in_degrees:
                in_degrees[v] = 0

    # 각 간선을 확인하며 진입 차수를 증가시킴
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1

    # 2. 진입 차수가 0인 모든 정점을 큐에 추가
    queue = deque([u for u, degree in in_degrees.items() if degree == 0])

    # 위상 정렬 결과를 저장할 리스트
    topological_order = []

    # 3. 메인 루프: 큐가 빌 때까지 반복
    while queue:
        # 큐에서 정점을 하나 꺼내 결과 리스트에 추가
        u = queue.popleft()
        topological_order.append(u)

        # 현재 정점 u와 연결된 모든 이웃 정점 v를 확인
        # graph.get(u, [])는 u가 키로 없을 경우(나가는 간선이 없는 경우)를 대비
        for v in graph.get(u, []):
            # u에서 v로의 간선을 "제거"한 것으로 간주하고, v의 진입 차수를 1 감소
            in_degrees[v] -= 1

            # 만약 v의 진입 차수가 0이 되었다면, 큐에 추가
            if in_degrees[v] == 0:
                queue.append(v)

    # 4. 사이클(Cycle) 확인 및 결과 반환
    # 만약 위상 정렬된 정점의 수가 전체 정점의 수와 다르다면, 사이클이 존재함
    if len(topological_order) == len(in_degrees):
        return topological_order
    else:
        return "그래프에 사이클이 존재하여 위상 정렬을 완료할 수 없습니다."

# --- 실행 부분 ---

# 인접 리스트로 구현 벨만 포드 빼고 다 인접리스트로 구현하고 벨만은 edge list로
G = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': []  # 'F'는 나가는 간선이 없음
}

print("슬라이드 예시 그래프 G의 위상 정렬 결과:")
result = kahn_topological_sort(G)
print(result)

print("-" * 40)

# 사이클이 있는 그래프 예시
G_cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']  # A -> B -> C -> A 사이클
}

print("사이클이 있는 그래프 G_cycle의 위상 정렬 결과:")
result_cycle = kahn_topological_sort(G_cycle)
print(result_cycle)