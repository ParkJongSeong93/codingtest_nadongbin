import sys

n, L = map(int, sys.stdin.readline().split())
G = list(map(int, sys.stdin.readline().split()))

total = G[-1]
count = 1
broken = False

for i in range(n - 2, -1, -1):
    calculated_G = total / count

    if not (G[i] - L < calculated_G < G[i] + L):
        broken = True
        break

    total += G[i]
    count += 1

print('unstable' if broken else 'stable')