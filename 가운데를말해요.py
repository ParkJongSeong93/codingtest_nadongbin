import sys
import heapq

N = int(sys.stdin.readline())

left = []   # 최대 힙처럼 사용(음수 저장)
right = []  # 최소 힙

for _ in range(N):
    num = int(sys.stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and -left[0] > right[0]:
        l = -heapq.heappop(left)
        r = heapq.heappop(right)
        heapq.heappush(left, -r)
        heapq.heappush(right, l)

    print(-left[0])