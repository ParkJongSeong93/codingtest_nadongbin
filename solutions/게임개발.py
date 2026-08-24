# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례로 갈 곳을 정함
# 아직 가보지 않았다면 왼쪽 한 칸 전진, 가봤다면 회전만
# 4방향 모두 가봤다면 바라보는 방향을 유지한 채로 1칸 뒤로 감, 만약 뒤가 바다라면 종료
# 맵의 외곽은 항상 바다, 1이 바다, 0이 육지

n, m = map(int, input().split())

r, c , dir = map(int, input().split())
# 방향 설정
dirArray = [(-1,0),(0,1),(1,0),(0,-1)]

# 이중 리스트 입력
gameMap = [list(map(int, input().split())) for _ in range(n)]
# 이중 리스트 선언
visited = [[0]*m for _ in range(n)]

visited[r][c] = 1

answer = 1
rotateCount = 0
def rotate():
    global dir, rotateCount
    dir = (dir + 3) % 4
    rotateCount += 1

while True:
    rotate()
    nr = r + dirArray[dir][0]
    nc = c + dirArray[dir][1]

    # 갈 수 있다면 전진(육지이고 방문하지 않은 곳이라면)
    if gameMap[nr][nc] == 0 and visited[nr][nc] == 0:
        r = nr
        c = nc
        visited[r][c] = 1
        answer += 1
        rotateCount = 0
        continue
    
    # 갈 수 없는 경우
    # 만약 4번 rotate한 경우
    if rotateCount == 4:
        nr = r - dirArray[dir][0]
        nc = c - dirArray[dir][1]
        # 뒤에 육지인 경우 갈 수 있음
        if gameMap[nr][nc] == 0:
            r = nr
            c = nc
            rotateCount = 0
            continue
        # 뒤에 바다인 경우
        break
        
print(answer)