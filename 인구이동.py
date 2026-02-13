from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

answer = 0

N, L, R = map(int, input().split())

heads = []
for _ in range(N):
    heads.append(list(map(int, input().split())))

def process():
    global N, L, R, heads, answer

    more = False

    visited = [[False] * N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue

            # 주위의 나라들과 연합이 가능한지 체크
            can_be_union = False
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                if (L <= abs(heads[r][c] - heads[nr][nc]) <= R):
                    can_be_union = True
                    break

            # 연합들 연산
            if can_be_union:
                more = True

                sum = [(r,c)]
                sum_num = heads[r][c]

                q = deque()
                q.append((r,c))
                visited[r][c] = True

                while q:
                    current_r, current_c = q.popleft()
                    for i in range(4):
                        nr = current_r + dr[i]
                        nc = current_c + dc[i]
                        if nr < 0 or nr >= N or nc < 0 or nc >= N:
                            continue
                        if (L <= abs(heads[current_r][current_c] - heads[nr][nc]) <= R) == False:
                            continue
                        if visited[nr][nc]:
                            continue
                        q.append((nr, nc))
                        visited[nr][nc] = True
                        sum.append((nr, nc))
                        sum_num += heads[nr][nc]

                for (r_in_sum,c_in_sum) in sum:
                    heads[r_in_sum][c_in_sum] = sum_num // len(sum)
                
    if more:
        answer += 1
        return True
    else:
        return False

while True:
    if process() == False:
        break

print(answer)