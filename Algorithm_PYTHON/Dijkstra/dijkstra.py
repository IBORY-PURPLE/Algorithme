import heapq

def dijkstra(graph, start):
    """
    다익스트라 알고리즘을 구현한 함수입니다.

    Args:
        graph (dict): 노드와 인접 노드 간의 가중치를 나타내는 그래프
        start: 시작 노드

    Returns:
        tuple: (최단 거리 딕셔너리, 이전 노드 딕셔너리)
    """
    # 1. 초기화
    # 모든 노드까지의 거리를 무한대(inf)로 초기화
    distances = {node: float('inf') for node in graph}
    # 이전 노드를 기록하기 위한 딕셔너리
    predecessors = {node: None for node in graph}
    # 시작 노드의 거리는 0으로 설정
    distances[start] = 0
    # 우선순위 큐에 (거리, 노드) 형태로 시작 노드를 추가
    priority_queue = [(0, start)]
    # 최단 거리가 확정된 노드를 기록할 집합(set)
    visited = set()

    while priority_queue:
        # 2. 우선순위 큐에서 가장 거리가 짧은 노드를 꺼냄
        current_distance, current_node = heapq.heappop(priority_queue)

        # 이미 최단 거리가 확정된 노드라면 건너뜀
        if current_node in visited:
            continue

        # 3. 해당 노드의 최단 거리를 확정하고 방문 처리
        # heappop 이후에 visited에 추가하는 것이 논리적으로 올바른 위치입니다.
        visited.add(current_node)

        # 4. 현재 노드와 인접한 노드들의 거리를 확인하고 업데이트
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 현재 노드를 거쳐 가는 것이 기존 경로보다 짧은 경우
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                # 우선순위 큐에 업데이트된 거리와 노드 정보를 추가
                # 실제 C단계에서 pq리스트를 구하면 pq =[(7,'z'), (8,'t'), (14,'x'), (10, 't')]
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

def get_path(predecessors, start, end):
    """
    이전 노드 정보를 바탕으로 최단 경로를 역추적하는 함수입니다.
    """
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()  # 경로를 start -> end 순으로 뒤집음
    return path

# 사용자께서 제공한 그래프
graph = {
    's' : {'t':10, 'y':5},
    't' : {'x':1, 'y':2},
    'y' : {'t':3, 'x':9, 'z':2},
    'x' : {'z':4},
    'z' : {'s':7, 'x':6}
}

# 시작 노드와 종료 노드 설정
start_node = 's'
end_node = 'x'

# 다익스트라 알고리즘 실행
final_distances, prev_nodes = dijkstra(graph, start_node)

# 결과 출력
shortest_path = get_path(prev_nodes, start_node, end_node)

print(f"'{start_node}'에서 다른 모든 노드까지의 최단 거리:")
print(final_distances)
print("-" * 30)
print(f"'{start_node}'에서 '{end_node}'까지의 최단 경로: {shortest_path}")
print(f"총 거리: {final_distances[end_node]}")