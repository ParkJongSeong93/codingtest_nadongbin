import sys

N = int(sys.stdin.readline())

data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()


## 반올림 처리법
data_sum = int(sum(data) / N + 0.5)
# round는 짝수쪽으로 감. 완전한 반올림이 아님
print(data_sum)
print(data[N//2])

appear_list = []
count = 0
for i in range(len(data)):
    if i == 0:
        count += 1
    elif i == len(data)-1:
        if data[i-1] == data[i]:
            count += 1
            appear_list.append((count, data[i]))
        else:
            appear_list.append((count, data[i-1]))
            appear_list.append((1, data[i]))
    else:
        if data[i-1] == data[i]:
            count += 1
        else:
            appear_list.append((count, data[i-1]))
            count = 1

    if len(data) == 1:
        appear_list.append((1, data[i]))

appear_list.sort(key=lambda item: (-item[0], item[1]))

if len(appear_list) >= 2 and appear_list[0][0] == appear_list[1][0]:
    most_appear_value = appear_list[1][1]
else:
    most_appear_value = appear_list[0][1]

print(most_appear_value)
print(data[-1] - data[0])