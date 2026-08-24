G = int(input())
P = int(input())

parent = [i for i in range(G + 1)]  # 0은 더 이상 배정 불가(종료 신호)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[a] = b  # a를 사용했으니 이제 a의 대표를 b로

count = 0
for _ in range(P):
    g = int(input())
    gate = find(g)       # g 이하에서 가능한 최대 게이트
    if gate == 0:        # 더 이상 배정 불가 -> 이후도 전부 불가
        break
    union(gate, gate-1)  # gate 사용 처리
    count += 1

print(count)