from collections import defaultdict

graph = defaultdict(list)
graph[1].append((2, 5))  # 1 → 2, 비용 5
graph[1].append((3, 2))  # 1 → 3, 비용 2
graph[2].append((3, 1))  # 2 → 3, 비용 1
graph[2].append((4, 2))  # 2 → 4, 비용 2
graph[3].append((4, 3))  # 3 → 4, 비용 3

for node, edges in graph.items():
    print(f"{node} -> {edges}")