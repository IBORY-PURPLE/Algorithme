def knapsack_suffix_top_down(i, rem_w, values, weights, memo):
    """
    i번째 아이템부터 마지막 아이템까지 고려했을 때,
    남은 무게 rem_w로 담을 수 있는 최대 가치를 반환합니다.
    """
    # 기본 케이스(Base Case): 더 이상 고려할 아이템이 없거나 무게가 0이면 0을 반환
    if i >= len(values) or rem_w <= 0:
        return 0

    # 이미 계산된 값이 있다면 그 값을 반환 (Memoization)
    if memo[i][rem_w] != -1:
        return memo[i][rem_w]

    # 1. 현재 i번째 아이템을 담지 않는 경우
    # 다음 아이템(i+1)부터 고려하고, 남은 무게는 그대로.
    res_not_take = knapsack_suffix_top_down(i + 1, rem_w, values, weights, memo)

    # 2. 현재 i번째 아이템을 담는 경우
    res_take = 0
    # 현재 아이템의 무게가 남은 무게보다 작거나 같아야 담을 수 있음
    if weights[i] <= rem_w:
        # 현재 아이템의 가치 + (다음 아이템부터 고려, 남은 무게는 현재 아이템 무게만큼 감소)
        res_take = values[i] + knapsack_suffix_top_down(i + 1, rem_w - weights[i], values, weights, memo)

    # 두 경우 중 더 큰 가치를 선택하여 메모하고 반환
    memo[i][rem_w] = max(res_not_take, res_take)
    return memo[i][rem_w]

# --- 실행 코드 ---
values = [60, 100, 120]
weights = [10, 20, 30]
max_weight = 50
n = len(values)

# 메모이제이션을 위한 2D 배열 초기화 (-1은 아직 계산되지 않았음을 의미)
# 행: 아이템 인덱스, 열: 남은 무게
memo = [[-1 for _ in range(max_weight + 1)] for _ in range(n + 1)]

# 초기 호출: 0번째 아이템부터 시작, 최대 무게 W를 가지고 시작
max_value = knapsack_suffix_top_down(0, max_weight, values, weights, memo)

print(f"최대 담을 수 있는 가치: {max_value}") # 예상 결과: 220 (100 + 120)