import sys

T = int(sys.stdin.readline())

def main():
    n, m = map(int, sys.stdin.readline().split())
    gold_mine = [[0] * m for _ in range(n)]
    temp = list(map(int, sys.stdin.readline().split()))
    
    for i in range(n * m):
        gold_mine[i // m][i % m] = temp[i]

    for c in range(1, m):
        for r in range(n):
            t1 = gold_mine[r-1][c-1] if r-1 >= 0 else 0
            t2 = gold_mine[r][c-1]
            t3 = gold_mine[r+1][c-1] if r+1 < n else 0
            gold_mine[r][c] += max(t1, t2, t3)
    
    answer = 0
    for r in range(n):
        answer = max(answer, gold_mine[r][m-1])
    print(answer)

for _ in range(T):
    main()