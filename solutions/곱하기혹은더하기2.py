nums = input()

answer = 0
for n in nums:
    n = int(n)
    if n == 0 or n == 1 or answer == 0:
        answer += n
    else:
        answer *= n

print(answer)