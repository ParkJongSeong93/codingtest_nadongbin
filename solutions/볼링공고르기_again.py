import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    weight_num = [0] * (M+1)
    answer = 0
    balls = list(map(int, input().split()))

    for ball in balls:
        weight_num[ball] += 1

    for i in range(1, len(weight_num)):
        answer += weight_num[i] * (sum(weight_num) - weight_num[i])

    print(answer//2)

main()