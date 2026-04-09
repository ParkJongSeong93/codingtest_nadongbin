import sys

N, M = map(int, sys.stdin.readline().split())

parent = [i for i in range(N)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

is_connected = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if is_connected[i][j] == 1:
            union(parent, i, j)

wanna_go = list(map(int, sys.stdin.readline().split()))
is_available = True
# 0-based, 1-based 구분 잘하기
P = find_parent(parent, wanna_go[0] - 1)
for i in range(1, len(wanna_go)):
    if P != find_parent(parent, wanna_go[i] - 1):
        is_available = False
        break

print('YES' if is_available else 'NO')