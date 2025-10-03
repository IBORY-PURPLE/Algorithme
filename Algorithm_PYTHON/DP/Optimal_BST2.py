import sys

def optimal_bst(keys, probabilities):
    """
    주어진 키와 확률을 바탕으로 최적 이진 탐색 트리를 구성하고,
    그 과정과 결과를 출력하는 함수.

    Args:
        keys (list): 키 값들의 리스트.
        probabilities (list): 각 키의 검색 확률 리스트.
    """
    # 1. 입력 처리 및 정렬
    # 키와 확률을 묶은 후 키를 기준으로 정렬합니다.
    sorted_pairs = sorted(zip(keys, probabilities))

    # 1-based indexing을 위해 맨 앞에 더미 값을 추가합니다.
    # p[i]는 k[i]의 확률을 의미합니다.
    k = [0] + [pair[0] for pair in sorted_pairs]
    p = [0.0] + [pair[1] for pair in sorted_pairs]

    n = len(k) - 1
    if n == 0:
        print("키가 없습니다.")
        return

    print("--- 입력 데이터 (정렬 후) ---")
    print(f"Keys (k): {k[1:]}")
    print(f"Probabilities (p): {p[1:]}\n")

    # 2. DP 테이블 초기화
    # e[i][j]: k[i]...k[j]로 만드는 최적 BST의 최소 비용
    # w[i][j]: p[i]...p[j]의 합
    # root[i][j]: k[i]...k[j]로 만드는 최적 BST의 루트 인덱스
    e = [[0.0 for _ in range(n + 2)] for _ in range(n + 2)]
    w = [[0.0 for _ in range(n + 2)] for _ in range(n + 2)]
    root = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # w 테이블과 e 테이블의 기본값(길이 1)을 초기화
    for i in range(1, n + 2):
        # j = i - 1 일 때 e와 w는 0
        e[i][i-1] = 0.0
        w[i][i-1] = 0.0
        if i <= n:
            # 부분 문제의 길이가 1일 때
            e[i][i] = p[i]
            w[i][i] = p[i]
            root[i][i] = i

    # 확률 합(w) 테이블 미리 계산
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            w[i][j] = w[i][j-1] + p[j]