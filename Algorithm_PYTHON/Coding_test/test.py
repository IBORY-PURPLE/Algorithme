# import sys
# from collections import defaultdict, deque

# # sys.stdin.readline을 사용하기 위한 설정 (더 빠른 입력)
# input = sys.stdin.readline

# def topological_sort(N, G, In):
#     """
#     위상정렬을 수행하여 작업 순서 리스트를 반환합니다.
#     In 배열의 복사본을 만들어 사용합니다. (원본 훼손 방지)
#     """
#     In_copy = In[:]  # 진입 차수 배열 복사
#     q = deque()
#     order = []  # 위상정렬 순서

#     # 1. 진입 차수가 0인 노드(시작 작업)를 큐에 추가
#     for i in range(1, N + 1):
#         if In_copy[i] == 0:
#             q.append(i)

#     # 2. 큐를 돌면서 위상정렬 수행
#     while q:
#         u = q.popleft()
#         order.append(u)

#         for v in G[u]:
#             In_copy[v] -= 1
#             if In_copy[v] == 0:
#                 q.append(v)

#     return order

# def find_completion_time(N, G, task_times, order):
#     """
#     위상정렬된 순서를 기반으로 DAG의 최장 경로(최대 완료 시간)를 찾습니다.
#     """
#     # dp_start[i] = i번 작업의 '시작 시간'
#     dp_start = [0] * (N + 1)
#     # dp_finish[i] = i번 작업의 '완료 시간'
#     dp_finish = [0] * (N + 1)

#     # 위상정렬된 순서대로 노드를 처리
#     for u in order:
#         # 1. 현재 작업(u)의 완료 시간 계산
#         # (현재 작업의 시작 시간 + 현재 작업의 소요 시간)
#         dp_finish[u] = dp_start[u] + task_times[u]

#         # 2. 현재 작업(u)이 끝났으므로, 후행 작업(v)들의 시작 시간 갱신
#         for v in G[u]:
#             # v의 시작 시간은, v의 모든 선행 작업(u)들의
#             # 완료 시간 중 가장 큰 값(가장 늦게 끝나는 시간)이 됩니다.
#             dp_start[v] = max(dp_start[v], dp_finish[u])

#     # 모든 작업의 '완료 시간' 중 가장 큰 값이
#     # 전체 프로젝트가 완료되는 시간입니다.
#     return max(dp_finish)

# if __name__ == "__main__":
#     # 1. 노드(작업) 갯수 N, 간선(선후 관계) 갯수 M 입력
#     print("노드(작업) 갯수와 간선(선후 관계) 갯수를 입력하세요 (예: 7 8):")
#     N, M = map(int, input().split())

#     # 2. 각 노드(작업)의 소요 시간 입력 (N개)
#     # (1번 노드부터 N번 노드까지의 시간을 공백으로 구분하여 입력)
#     print(f"1번부터 {N}번까지 각 작업의 소요 시간을 입력하세요 (예: 10 20 5 ...):")
#     # task_times[0]은 사용하지 않고, 1-based 인덱싱을 위해 0을 추가
#     task_times = [0] + list(map(int, input().split()))

#     # 그래프 자료구조 초기화
#     G = defaultdict(list)  # 인접 리스트 (가중치 X, 방향만)
#     In = [0] * (N + 1)     # 진입 차수 배열

#     # 3. M개의 간선(선후 관계) 입력
#     print(f"{M}개의 선후 관계를 입력하세요 (예: '선행작업 후행작업'):")
#     for _ in range(M):
#         u, v = map(int, input().split())
#         G[u].append(v)  # u -> v
#         In[v] += 1      # v의 진입 차수 증가

#     # --- 알고리즘 실행 ---

#     # 1. 위상정렬 수행
#     # (N개의 노드를 모두 방문하기 전에 큐가 비면 사이클이 존재)
#     order = topological_sort(N, G, In)

#     if len(order) != N:
#         print("그래프에 사이클이 존재합니다. (DAG가 아님)")
#     else:
#         # 2. 위상정렬 순서를 기반으로 전체 완료 시간 계산
#         total_time = find_completion_time(N, G, task_times, order)

#         print("\n--- 결과 ---")
#         print(f"작업 순서: {order}")
#         print(f"전체 프로젝트 완료에 필요한 최소 시간: {total_time}")


from collections import defaultdict
import sys

graph = defaultdict(list)
graph[1].append((2, 5))  # 1 → 2, 비용 5
graph[1].append((3, 2))  # 1 → 3, 비용 2
graph[2].append((3, 1))  # 2 → 3, 비용 1
graph[2].append((4, 2))  # 2 → 4, 비용 2
graph[3].append((4, 3))  # 3 → 4, 비용 3

for node, edges in graph.items():
    print(f"{node} -> {edges}")

input = sys.stdin.readline
for _ in range(N):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

edges = [
    (1, 2, 5),  # 1 → 2, 가중치 5
    (1, 3, 2),  # 1 → 3, 가중치 2
    (2, 3, 1),  # 2 → 3, 가중치 1
    (2, 4, 2),  # 2 → 4, 가중치 2
    (3, 4, 3)   # 3 → 4, 가중치 3
]

for u, v, w in edges:
    print(f"{u} → {v}, weight = {w}")

for _ in range(N):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))