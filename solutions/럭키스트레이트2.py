N = input()

pivot = len(N) // 2
left_sum = 0
right_sum = 0

for i in range(len(N)):
    if i < pivot:
        left_sum += int(N[i])
    else:
        right_sum += int(N[i])

print('LUCKY' if right_sum == left_sum else 'READY')