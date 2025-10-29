import sys

def solve():
    """
    플로이드-워셜 알고리즘을 사용하여 모든 쌍의 최단 경로를 계산하고,
    """
    input = sys.stdin.readline
    first_case = True
    while True:
        try:
            line = input()
            if not line:
                break

            n, m, q = map(int, line.split())
            if n == 0 and m == 0 and q == 0:
                break

            if not first_case:
                print()
            first_case = False

            # 거리 행렬 초기화
            inf = float('inf')
            dist = [[inf] * n for _ in range(n)]
            for i in range(n):
                dist[i][i] = 0

            # 간선 정보 입력
            for _ in range(m):
                u, v, w = map(int, input().split())
                dist[u][v] = min(dist[u][v], w)

            # 플로이드-워셜 알고리즘
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if dist[i][k] != inf and dist[k][j] != inf:
                            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

            # 음수 사이클 감지 및 처리
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        if dist[i][k] != inf and dist[k][j] != inf and dist[k][k] < 0:
                            dist[i][j] = -inf

            # 쿼리 처리 및 출력
            for _ in range(q):
                u, v = map(int, input().split())
                if dist[u][v] == inf:
                    print("Impossible")
                elif dist[u][v] == -inf:
                    print("-Infinity")
                else:
                    print(dist[u][v])

        except (IOError, ValueError):
            break

if __name__ == "__main__":
    solve()