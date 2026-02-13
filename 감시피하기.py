n = int(input())

grid = []
for _ in range(n):
    grid.append(list(input().split()))

teachers = []
for r in range(n):
    for c in range(n):
        if grid[r][c] == 'T':
            teachers.append((r,c))

def check_hide_available(teachers, grid):
    grid_size = len(grid)
    for (r,c) in teachers:
        # 남쪽 탐색
        for i in range(r+1, grid_size):
            if grid[i][c] == 'S':
                return False
            elif grid[i][c] == 'O':
                break
        # 북쪽 탐색
        for i in range(r-1, -1, -1):
            if grid[i][c] == 'S':
                return False
            elif grid[i][c] == 'O':
                break
        # 서쪽 탐색
        for i in range(c-1, -1, -1):
            if grid[r][i] == 'S':
                return False
            elif grid[r][i] == 'O':
                break
        # 동쪽 탐색
        for i in range(c+1, grid_size):
            if grid[r][i] == 'S':
                return False
            elif grid[r][i] == 'O':
                break
    return True

answer = False
def dfs(idx, count):
    global teachers, grid, n, answer

    if answer == True:
        return True

    if count == 3:
        if(check_hide_available(teachers, grid) == True):
            return True
        else:
            return False
        
    for i in range(idx, n*n):
        r = i // n
        c = i % n
        if grid[r][c] == 'X':
            grid[r][c] = 'O'
            if (dfs(i+1, count+1) == True):
                answer = True
                break
            grid[r][c] = 'X'
       
    if answer == True:
        return True
    else:
        return False

if (dfs(0, 0) == True):
    print('YES')
else:
    print('NO')