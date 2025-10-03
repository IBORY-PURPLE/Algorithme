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

    # 3. 상향식 계산
    # l은 부분 문제의 길이 (체인의 길이)
    print("--- DP 테이블 계산 과정 ---")
    for l in range(2, n + 1):  # 길이가 2인 서브트리부터 n까지
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i][j] = sys.float_info.max # 최솟값을 찾기 위해 무한대로 초기화

            print(f"\n[e[{i}][{j}]] 계산 (키: {k[i]}..{k[j]})")
            print(f"  - 확률 합 w[{i}][{j}] = {w[i][j]:.2f}")

            # i와 j 사이의 모든 키를 루트(r) 후보로 시도
            for r in range(i, j + 1):
                # 점화식: e[i,j] = e[i,r-1] + e[r+1,j] + w(i,j)
                cost = e[i][r-1] + e[r+1][j] + w[i][j]

                print(f"  - 루트 후보 r={r} (키:{k[r]}): cost = e[{i}][{r-1}] + e[{r+1}][{j}] + w[{i}][{j}]")
                print(f"    -> {'%.2f' % e[i][r-1]} + {'%.2f' % e[r+1][j]} + {'%.2f' % w[i][j]} = {'%.2f' % cost}")

                if cost < e[i][j]:
                    e[i][j] = cost
                    root[i][j] = r
                    print(f"    >> 새로운 최소 비용 발견! e[{i}][{j}] = {'%.2f' % cost}, root = {r} (키:{k[r]})")

    print("\n\n--- 최종 DP 테이블 ---")
    print("최소 비용 테이블 (e):")
    for i in range(1, n + 2):
        for j in range(n + 1):
            if j >= i - 1:
                print(f"{e[i][j]:.2f}\t", end="")
            else:
                print("    \t", end="")
        print()

    print("\n최적 루트 테이블 (root):")
    for i in range(1, n + 1):
        for j in range(n + 1):
             if j >= i:
                 print(f"{root[i][j]}\t", end="")
             else:
                 print(" \t", end="")
        print()

    print(f"\n\n--- 최종 결과 ---")
    print(f"전체 키에 대한 최소 기대 검색 비용: {e[1][n]:.2f}")

    # 4. 트리 재구성 및 출력
    print("\n--- 최적 이진 탐색 트리 구조 ---")

    # 17번 슬라이드의 CONSTRUCT-OPT-SUBTREE 의사코드를 재귀 함수로 구현
    def construct_tree(i, j, parent_r, side):
        if i > j:
            return

        # 현재 서브트리의 루트를 찾음
        r = root[i][j]

        if parent_r == 0: # 전체 트리의 루트일 경우
            print(f"'{k[r]}'는(은) 전체 트리의 루트입니다.")
        else:
            print(f"'{k[r]}'는(은) 부모 '{k[parent_r]}'의 {side} 자식입니다.")

        # 재귀적으로 왼쪽과 오른쪽 서브트리를 구성
        construct_tree(i, r - 1, r, "왼쪽")
        construct_tree(r + 1, j, r, "오른쪽")

    # 재귀 함수 호출 시작
    initial_root_r = root[1][n]
    if initial_root_r != 0:
        construct_tree(1, n, 0, "루트")
    else:
        print("트리를 구성할 수 없습니다.")


# --- 예제 실행 ---
# 슬라이드 5, 6페이지의 예제 데이터
keys_example = [1, 2, 3, 4, 5]
probs_example = [0.25, 0.2, 0.05, 0.2, 0.3] # p1, p2, p3, p4, p5

# 함수 실행
optimal_bst(keys_example, probs_example)