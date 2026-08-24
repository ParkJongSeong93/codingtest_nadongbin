# x가 주어질 때, [5,3,2]로 나눠 떨어지면 그 수로 나눈다. 그것이 아니라면 1을 뺀다
# 최소 연산 수 구하기

x = int(input())

array = [0] * (x + 1)
for i in range(2, x+1):
    array[i] = array[i-1] + 1

    # 여러개로 나눠떨어질 수 있고 그것들을 모두 비교해야하기 때문에 elif 사용은 적절X
    if i % 5 == 0:
        array[i] = min(array[i], array[i//5]+1)
    if i % 3 == 0:
        array[i] = min(array[i], array[i//3]+1)
    if i % 2 == 0:
        array[i] = min(array[i], array[i//2]+1)

print(array[x])
