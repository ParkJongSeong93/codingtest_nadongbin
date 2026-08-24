n = int(input())
travelers = list(map(int, input().split()))
travelers.sort()

# 앞에서부터 돌면서 현재 공포도와 모인 수를 비교해서 그룹화 가능한지 체크
members_count = 0
groups_count = 0
for i in travelers:
    members_count += 1
    # 현재 공포도 이상의 멤버들이 모이면 그룹 가능
    if members_count >= i:
        groups_count += 1
        members_count = 0

print(groups_count)