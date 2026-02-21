def solution(n):
    answer = 0
    num = 1
    for _ in range(n):
        answer += num
        num += 2*(n-1)

    return answer

n1 = 3
ret1 = solution(n1)

print(f"solution1 함수의 반환 값은 {ret} 입니다")

