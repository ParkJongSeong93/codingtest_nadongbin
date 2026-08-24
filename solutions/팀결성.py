# 0~n번까지의 번호를 부여받은 학생들
# 처음엔 모두 다른 팀으로 구분
# 팀 합치기 연산, 같은 팀 여부 확인 연산만 사용 가능
# m개의 연산, 같은 팀 여부 확인 시에는 출력

n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

def find_parent(a):
    if a == parent[a]:
        return a
    else:
        # 경로 압축
        parent[a] = find_parent(parent[a])
        return parent[a]

def union_team(a, b):
    # 루트 parent를 찾고 진행
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    mode, a, b = map(int, input().split())
    if mode == 0:
        union_team(a, b)
    else:
        answer = "YES" if find_parent(a) == find_parent(b) else "NO"
        print(answer)