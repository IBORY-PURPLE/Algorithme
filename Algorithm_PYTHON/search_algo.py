N = 3   # 부분집합을 만들 집합의 원소 개수
subset = []  # 현재 부분집합 저장

def print_subset(subset):
    print("{", " ".join(map(str, subset)), "}")

def search(k):
    if k > N:
        # 종료 조건: 1 ~ N까지 포함 여부를 다 정했을 때
        print_subset(subset)
    else:
        # 1. k를 포함하는 경우
        subset.append(k)
        search(k + 1)

        # 2. k를 포함하지 않는 경우
        subset.pop()
        search(k + 1)

# 실행
search(1)
