import sys


# if __name__ == "__main__":
#     N, M = map(int, sys.stdin.readline().split())

#     pocket = [i for i in range(N+1)]

#     for _ in range(M):
#         num1, num2 = map(int, sys.stdin.readline().split())
#         pocket[num1], pocket[num2] = pocket[num2], pocket[num1]

#     print(" ".join(map(str, pocket[1:])))

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    pocket = [i for i in range(N+1)]

    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        pocket[start:end+1] = pocket[start:end+1][::-1]

    print(" ".join(map(str, pocket[1:])))
