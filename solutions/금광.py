T = int(input())

for test_case in range(T):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    grid = [[0] * m for _ in range(n)]
    for i in range(n*m):
        r = i // m
        c = i % m
        grid[r][c] = data[i]
    
    # 마지막 열에서 시작하는 값이 있으니 초기 정답은 마지막 열 최댓값
    total_max_value = max(grid[r][m-1] for r in range(n))
    # 뒤쪽 열에서부터 앞으로 가면서 최댓값 저장
    for c in range(m-2, -1, -1):
        for r in range(n):
            # 오른쪽 위, 오른쪽, 오른쪽 아래 값을 더한 값들 중 최대
            if r == 0:
                max_value = max(grid[r][c+1], grid[r+1][c+1])
            elif r == n-1:
                max_value = max(grid[r-1][c+1], grid[r][c+1])
            else:
                max_value = max(grid[r-1][c+1], grid[r][c+1], grid[r+1][c+1])
            grid[r][c] += max_value
            total_max_value = max(grid[r][c], total_max_value)
    
    print(total_max_value)