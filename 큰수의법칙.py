# 큰 수의 법칙
# n은 배열의 크기, m은 숫자가 더해지는 횟수, k는 연속으로 덧셈이 가능한 최대 수

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

answer = 0

for i in range(1, m+1):
    if(i % (k+1) == 0): answer += second
    else: answer += first

print(answer)