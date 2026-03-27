import sys
import heapq

def main():
    N = int(sys.stdin.readline())
    hq = []
    answer = 0

    for _ in range(N):
        heapq.heappush(hq, int(sys.stdin.readline()))

    while len(hq) > 1:
        sum = heapq.heappop(hq) + heapq.heappop(hq)
        answer += sum
        heapq.heappush(hq, sum)

    print(answer)

main()