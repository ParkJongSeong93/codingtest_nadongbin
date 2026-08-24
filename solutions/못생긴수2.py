import sys
import heapq

hq = []
heapq.heappush(hq, 1)

visited = set()
visited.add(1)

n = int(sys.stdin.readline())
answer = 1
for i in range(1, n+1):
    answer = heapq.heappop(hq)
    
    t1 = answer * 2
    if t1 not in visited:
        heapq.heappush(hq, t1)
        visited.add(t1)

    t2 = answer * 3
    if t2 not in visited:
        heapq.heappush(hq, t2)
        visited.add(t2)

    t3 = answer * 5
    if t3 not in visited:
        heapq.heappush(hq, t3)
        visited.add(t3)

print(answer)
