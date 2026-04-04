import sys

G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

parent = [i for i in range(G+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    parent[a] = b

count = 0
for i in range(P):
    g_i = int(sys.stdin.readline())
    if find_parent(parent, g_i) == 0:
        break

    gate = find_parent(parent, g_i)
    union(parent, gate, gate - 1)
    count += 1

print(count)