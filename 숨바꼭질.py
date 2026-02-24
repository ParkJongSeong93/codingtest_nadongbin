import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = []
heapq.heappush(q, (0, 1))
visited = [False] * (N+1)
visited[1] = True

number = 1
answer_dist = 0
same_number = 1

while q:
    dist, current_node = heapq.heappop(q)
    for next_node in graph[current_node]:
        if visited[next_node]:
            continue
        heapq.heappush(q, (dist+1, next_node))
        visited[next_node] = True

        if dist+1 > answer_dist:
            answer_dist = dist+1
            same_number = 1
            number = next_node
        elif dist+1 == answer_dist:
            same_number += 1
            number = min(number, next_node)

print(number, answer_dist, same_number)    
