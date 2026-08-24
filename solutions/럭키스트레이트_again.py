N = input()

N_len = len(N)

first_part = 0
second_part = 0

for i in range(N_len // 2):
    first_part += int(N[i])

for i in range(N_len // 2, N_len):
    second_part += int(N[i])

if first_part == second_part:
    print("LUCKY")
else:
    print("READY")
