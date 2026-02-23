n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0

for i in range(1, n):
    nxt2 = ugly[i2] * 2
    nxt3 = ugly[i3] * 3
    nxt5 = ugly[i5] * 5

    nxt = min(nxt2, nxt3, nxt5)
    ugly[i] = nxt

    if nxt == nxt2:
        i2 += 1
    if nxt == nxt3:
        i3 += 1
    if nxt == nxt5:
        i5 += 1

print(ugly[n - 1])