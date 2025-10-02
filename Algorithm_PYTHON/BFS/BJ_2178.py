import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_r, start_c):
    queue = deque([(start_r, start_c)])

    miro[start_r][start_c] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if miro[nr][nc] == 1:
                miro[nr][nc] = miro[r][c] + 1
                queue.append((nr, nc))

    return miro[N-1][M-1]

if __name__ == "__main__":
    N, M = map(int, input().split())

    miro = [list(map(int, input().strip())) for _ in range(N)]

    print(bfs(0, 0))
