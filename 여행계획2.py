import sys

def main():
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

    N, M = map(int, sys.stdin.readline().split())
    parent = [i for i in range(N+1)]

    connect = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if connect[i][j] == 1:
                union(parent, i+1, j+1)

    wanna_go = list(map(int, sys.stdin.readline().split()))
    P = find_parent(parent, wanna_go[0])
    
    answer = True
    for i in range(1, M):
        if find_parent(parent, wanna_go[i]) != P:
            answer = False
            break

    print('YES' if answer else 'NO')

main()