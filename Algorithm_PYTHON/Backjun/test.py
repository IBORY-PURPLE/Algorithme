import sys

input = sys.stdin.readline

# str = input()

# N = int(input())

# print(str[N-1])

# ----------------------------------------------------------

# str = input().strip()
# cnt = 0

# for _ in str:
#     cnt += 1

# print(cnt)

# ----------------------------------------------------------

# N = int(input())

# for _ in range(N):
#     str = input().strip().upper()
#     print(str[0], str[-1], sep='')

# ----------------------------------------------------------

# N = int(input())
# str = input().strip()
# sum = 0
# nums = list(map(int, str))

# for i in nums:
#     sum += i

# print(sum)

str = (input().strip().lower())

ascii_list = [ord(char) for char in str]
result_list = [-1] * 26

for i in range(97, 123):
    find = False
    for j in range(len(ascii_list)):
        if ascii_list[j] == i and find == False:
            find = True
            result_list[i-97] = j

print(*result_list)

