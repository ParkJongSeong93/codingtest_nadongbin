import sys
input = sys.stdin.readline

def main():
    N = int(input())
    coins = list(map(int, input().split()))
    coins.sort()

    target = 1
    for coin in coins:
        if coin > target:
            break
        target += coin

    print(target)

main()