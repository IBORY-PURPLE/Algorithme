import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

testCase = int(input())

for i in range(testCase):
    stores = int(input())
    coordinates= []
    dist = [0] * (stores + 2)
    pq = []
    for i in range(stores + 2):
        x, y = map(int, input().split())
        coordinates.append((x, y))



