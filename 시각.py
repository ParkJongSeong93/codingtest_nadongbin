# 정수 n이 입력되면 n시 59분 59초까지 3이 하나라도 포함된 경우 수 구하기

n = int(input())
count = 0

for h in range(0, n+1):
    if '3' in str(h):
        count += 60*60
    else:
        for m in range(0, 60):
            if '3' in str(m):
                count += 60
            else:
                for s in range(0, 60):
                    if '3' in str(s):
                        count += 1

print(count)