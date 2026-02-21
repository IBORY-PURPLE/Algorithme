def func_a(numA, numB, exp):
    if (exp == "+"):
        return numA + numB
    elif (exp == "-"):
        return numA - numB
    elif (exp == "*"):
        return numA * numB

def func_b(exp):
    for index, value in enumerate(exp):
        if value == "+" or value == "-" or value == "*":
            return index

def func_c(exp, index):
    numA = int(exp[:index])
    numB = int(exp[index + 1:])
    return numA, numB


def solution(expression):
    #1단계 : 연산자의 index 알아내기
    exp_index = func_b(expression)
    #2단계 : 연산자 index기준으로 숫자 두개 추출하기
    first_num, second_num = func_c(expression, exp_index)
    #3단계 : 연산하기
    ret = func_a(first_num, second_num, expression[exp_index])
    return ret

if __name__ == "__main__":
    expression = "123+12"
    ret = solution(expression)

    print(f"solution 함수의 반환 값은 {ret} 입니다.")