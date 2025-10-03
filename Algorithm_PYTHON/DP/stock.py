def maxProfit_On(prices: list[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    # 주식을 보유했을 경우,
    # 주식을 팔았을 경우,
    # 아무것도 안했을 경우의 최대 이익을 저장할 배열 초기화
    hold = [0] * n
    sold = [0] * n
    rest = [0] * n

    # 0일차 때 초기값 세팅
    # hold한 경우가 주식을 구매한 경우이니깐 -값으로 세팅
    hold[0] = -prices[0]
    sold[0] = 0
    rest[0] = 0

    for i in range(1, n):
        # i번째 날에 주식을 보유한 경우의 최대 이익
        # (어제도 보유 vs 어제 휴식 후 오늘 매수)
        # sold하고는 cooldown을 가진다는 조건이 있으므로 sold경우에서는 올 수없다.
        hold[i] = max(hold[i-1], rest[i-1] - prices[i])

        # i번째 날에 주식을 매도한 경우의 최대 이익
        # (반드시 어제 보유했어야 함)
        sold[i] = hold[i-1] + prices[i]

        # i번째 날에 휴식한 경우의 최대 이익
        # (어제도 휴식 vs 어제 매도 후 오늘 cooldown)
        rest[i] = max(rest[i-1], sold[i-1])

    # 마지막 날, 매도했거나 휴식한 상태 중 최대 이익을 반환
    return max(sold[n-1], rest[n-1])


prices = [1, 2, 3, 0, 2]

print(f"최대 이익 : {maxProfit_On(prices)}")