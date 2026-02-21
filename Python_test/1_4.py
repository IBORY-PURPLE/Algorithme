def solution(num):
    return int(str(num+1).replace("0", "1"))


def solution_2(num):
    n = num + 1
    result = 0
    place = 1

    while n > 0:
        digit = n % 10
        if digit == 0:
            digit = 1
        result += digit * place
        place *= 10
        n //= 10

    return result

if __name__ == "__main__":
    num = 9949999
    ret = solution(num)
    ret_2 = solution_2(num)

    print(f"solution 함수의 반환 값은 {ret} 입니다.")
    print(f"solution_2 함수의 반환 값은 {ret_2} 입니다.")