import sys

# 메모이제이션을 위한 딕셔너리 (계산된 값을 저장)
memo = {}

def climbStairs(n):
    # 기본 사례
    if n == 1:
        return 1
    if n == 2:
        return 2

    # 이미 계산한 값이면 바로 반환
    if n in memo:
        return memo[n]

    # 점화식에 따라 재귀 호출하고 결과를 memo에 저장
    memo[n] = climbStairs(n - 1) + climbStairs(n - 2)
    return memo[n]

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    result = climbStairs(N)
    print(result)