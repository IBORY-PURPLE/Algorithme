def bellman_ford_with_edge_list(edge_list, vertices, source):
    # 1. 초기화
    distances = {vertex: float('inf') for vertex in vertices}
    distances[source] = 0
    predecessors = {vertex: None for vertex in vertices}

    num_vertices = len(vertices)

    # 2. (V-1)번 반복
    for i in range(num_vertices - 1):
        modified = False

        # ★ 여기가 다릅니다: 순수한 간선 리스트를 직접 순회
        for u, v, weight in edge_list:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
                modified = True

        if not modified:
            break

    # 3. 음수 사이클 확인
    # ★ 여기도 간선 리스트를 순회합니다.
    for u, v, weight in edge_list:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("그래프에 음수 가중치 사이클이 존재합니다.")
            return False, None, None

    return True, distances, predecessors

# --- 실행 ---
# 위에서 정의한 edge_list와 전체 정점 집합을 전달해야 함
edge_list = [
    ('s', 't', 6),
    ('s', 'y', 7),
    ('t', 'x', 5),
    ('t', 'y', 8),
    ('t', 'z', -4),
    ('y', 'x', -3),
    ('y', 'z', 9),
    ('x', 't', -2),
    ('z', 's', 2),
    ('z', 'x', 7)
]

all_vertices = {'s', 't', 'y', 'x', 'z'}
success, dist, pred = bellman_ford_with_edge_list(edge_list, all_vertices, 's')
# 결과는 동일합니다.