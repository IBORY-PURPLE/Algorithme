from collections import deque

def bfs(graph_adj, start_node):
    """
    너비 우선 탐색(BFS)을 수행하여 시작점으로부터 모든 정점까지의
    최단 경로 길이와 이전 정점을 찾습니다. (가중치 없는 그래프용)

    Args:
        graph_adj (dict): 인접 리스트 형태로 표현된 그래프
        start_node: 탐색을 시작할 정점

    Returns:
        tuple: (거리 딕셔너리 D, 이전 정점 딕셔너리 P)
    """
    UNVISITED = -1

    D = {v: UNVISITED for v in graph_adj}
    # D는 딕셔너리 자료형으로 graph_adj에 있는 키값마다 최단거리값을 대입하는 변수로 생각됨.
    # 예상 데이터 형태
    # {'s':[-1], 'r':[-1]}
    P = {v: None for v in graph_adj}
    # P는 딕셔너리 자료형으로 키값마다 해당 노드의 바로 전 노드를 저장해놓음.

    D[start_node] = 0

    queue = deque([start_node])
    # deque == double ended queue -> stack과 queue의 쓰임으로 같이 사용하기위한 유용한 함수
    # pop() -> 오른쪽 삭제 popleft -> 왼쪽삭제
    # append() -> 오른쪽 삽입 appendleft -> 왼쪽삽입

    while queue:
        u = queue.popleft()

        for neighbor in graph_adj[u]:
            if D[neighbor] == UNVISITED:
                D[neighbor] = D[u] + 1
                P[neighbor] = u
                queue.append(neighbor)

    return D, P

if __name__ == "__main__":
    sample_graph = {
        's': ['r', 'v', 'u'],
        'r': ['s', 'w', 't'],
        'v': ['s', 'w', 'y'],
        'u': ['s', 't', 'y'],
        'w': ['r','v', 'x', 'z'],
        'x': ['w', 'z'],
        'y': ['u', 'v', 'x'],
        't': ['r', 'u'],
        'z': ['w', 'x']
    }
    start = 's'

    distances, predecessors = bfs(sample_graph, start)

    print(f"'{start}' 정점에서 출발한 BFS결과")
    print("---" * 10)
    print("각 정점까지의 최단 거리 (D):")
    for node, dist in distances.items():
        print(f" {node}: {dist}")

    for node, pred in predecessors.items():
        print(f" {node}: {pred}")

