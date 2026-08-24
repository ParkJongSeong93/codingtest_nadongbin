import sys

N = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))
coins.sort()

target = 1
for coin in coins:
    if target < coin:
        print(target)
        break
    target += coin