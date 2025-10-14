import sys

def bellman_ford(graph, source):
    """
    개선된 벨만-포드 알고리즘을 사용하여 최단 경로를 찾습니다.

    Args:
        graph (dict): 인접 리스트 형태로 표현된 그래프.
                      예: {'u': {'v': weight}}
        source (str): 시작 정점(노드)

    Returns:
        tuple: (성공 여부, 거리 딕셔너리, 이전 정점 딕셔너리)
               성공 여부: 음수 사이클이 없으면 True, 있으면 False
               거리 딕셔너리: 시작점으로부터 각 정점까지의 최단 거리
               이전 정점 딕셔너리: 최단 경로를 역추적하기 위한 정보
    """
    # 1. 초기화
    # 모든 정점을 포함하도록 설정
    vertices = set(graph.keys())
    for u in graph:
        vertices.update(graph[u].keys())

    # 거리(D)는 모두 무한대(inf), 시작점만 0으로 초기화
    distances = {vertex: float('inf') for vertex in vertices}
    distances[source] = 0

    # 이전 정점(P)은 모두 None으로 초기화
    predecessors = {vertex: None for vertex in vertices}

    num_vertices = len(vertices)

    # 2. (V-1)번 반복하며 간선 릴렉세이션(Relaxation) 수행
    # 슬라이드 63의 for i=1 to N-1 부분
    for i in range(num_vertices - 1):
        modified = False  # 조기 종료를 위한 플래그 (슬라이드 63의 modified 변수)

        # 모든 간선 (u, v)에 대해 릴렉세이션 시도
        for u in graph:
            for v, weight in graph[u].items():
                # u를 거쳐 v로 가는 경로가 더 짧은 경우
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
                    modified = True # 거리가 갱신되었음을 표시

        # 만약 이번 반복에서 아무 거리도 갱신되지 않았다면,
        # 최단 경로가 이미 모두 찾아진 것이므로 조기 종료
        if not modified:
            print(f"최적화: {i + 1}번째 반복 후 변경이 없어 조기 종료합니다.")
            break

    # 3. 음수 가중치 사이클 확인
    # (V-1)번 반복 후에도 거리가 짧아지는 경로가 있다면 음수 사이클이 존재
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                print("그래프에 음수 가중치 사이클이 존재합니다.")
                return False, None, None  # 실패 반환

    # 음수 사이클이 없으면 성공(True)과 함께 결과 반환
    return True, distances, predecessors

# --- 실행 부분 ---

# 주어진 그래프 예시
graph = {
    's': {'t': 6, 'y': 7},
    't': {'x': 5, 'y': 8, 'z': -4},
    'y': {'x': -3, 'z': 9},
    'x': {'t': -2},
    'z': {'s': 2, 'x': 7}
}

# 시작점을 's'로 설정하여 알고리즘 실행
source_node = 's'
success, final_distances, final_predecessors = bellman_ford(graph, source_node)

# 결과 출력
if success:
    print("\n[알고리즘 실행 완료: 음수 사이클 없음]")
    print("-" * 40)
    print(f"시작점 '{source_node}'로부터의 최단 거리:")
    for vertex, distance in final_distances.items():
        print(f"  - 정점 {vertex}: {distance}")

    print("\n최단 경로 추적을 위한 이전 정점 정보:")
    for vertex, predecessor in final_predecessors.items():
        print(f"  - 정점 {vertex}: {predecessor}")