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

# str = (input().strip().lower())

# ascii_list = [ord(char) for char in str]
# result_list = [-1] * 26

# for i in range(97, 123):
#     find = False
#     for j in range(len(ascii_list)):
#         if ascii_list[j] == i and find == False:
#             find = True
#             result_list[i-97] = j

# print(*result_list)

# ----------------------------------------------------------

# N = int(input().strip())

# for _ in range(N):
#     num, s = input().split()
#     num = int(num)
#     result = []
#     for char in s:
#         for _ in range(num):
#             result.append(char)

#     print("".join(result))


# ----------------------------------------------------------

# s = input()

# word = s.strip().split()

# print(len(word))


# ----------------------------------------------------------

# num1, num2 = input().split()

# string_num1 = list(num1)
# string_num2 = list(num2)

# string_num1.reverse()
# string_num2.reverse()

# reversed_num1 = "".join(string_num1)
# reversed_num2 = "".join(string_num2)

# if reversed_num1 > reversed_num2:
#     print(reversed_num1)
# else :
#     print(reversed_num2)

# ----------------------------------------------------------

# mapping = {
#     "A": 2,
#     "B": 2,
#     "C": 2,
#     "D": 3,
#     "E": 3,
#     "F": 3,
#     "G": 4,
#     "H": 4,
#     "I": 4,
#     "J": 5,
#     "K": 5,
#     "L": 5,
#     "M": 6,
#     "N": 6,
#     "O": 6,
#     "P": 7,
#     "Q": 7,
#     "R": 7,
#     "S": 7,
#     "T": 8,
#     "U": 8,
#     "V": 8,
#     "W": 9,
#     "X": 9,
#     "Y": 9,
#     "Z": 9,
# }

# s = input().strip().upper()
# s_list = list(s)
# time = [0] * 10
# total_time = 0

# for i in range(1, 10):
#     if i == 1:
#         time[i] = 2
#     else :
#         time[i] += time[i-1] + 1

# for char in s_list:
#     total_time += time[mapping[char]]

# print(total_time)


# ----------------------------------------------------------

# s = []

# for _ in range(100):
#     line = input().strip()
#     if line == "":
#         break
#     s.append(line)

# print(" ".join(s))
# ----------------------------------------------------------

# n = int(input())

# for i in range(1, n+1):
#     print(' ' * (n - i) + '*' * (2*i - 1))

# for i in range(n-1, 0, -1):
#     print(' ' * (n - i) + '*' * (2*i - 1))


# ----------------------------------------------------------

# N, A = input().split()
# N = int(N)
# A = int(A)

# def sum_inverse(N, A):
#     for x in range(N):
#         if ((A+x) % N) == 0:
#             return x
#     return -1

# def multi_inverse(N, A):
#     for x in range(N):
#         if ((A * x) % N) == 1:
#             return x
#     return -1

# print(sum_inverse(N, A), multi_inverse(N, A))


# ----------------------------------------------------------


def extended_gcd(a: int, b: int):
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
    return old_r, old_x, old_y

def modinv(a: int, m: int):
    a %= m
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return -1
    return x % m

def addinv(a: int, m: int):
    return (-a) % m

N_str, A_str = sys.stdin.readline().split()
N = int(N_str); A = int(A_str)

print(addinv(A, N), modinv(A, N))

# ----------------------------------------------------------


# ----------------------------------------------------------


# ----------------------------------------------------------


# ----------------------------------------------------------

# ----------------------------------------------------------


# ----------------------------------------------------------

# ----------------------------------------------------------

# ----------------------------------------------------------

# ----------------------------------------------------------

# ----------------------------------------------------------
# ----------------------------------------------------------


# ----------------------------------------------------------


# ----------------------------------------------------------


# ----------------------------------------------------------


# ----------------------------------------------------------

# ----------------------------------------------------------


# ----------------------------------------------------------

