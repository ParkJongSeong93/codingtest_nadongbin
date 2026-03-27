import sys

N = int(sys.stdin.readline())
houses = list(map(int, sys.stdin.readline().split()))
houses.sort()

mid = N//2 -1 if N % 2 == 0 else N//2

print(houses[mid])