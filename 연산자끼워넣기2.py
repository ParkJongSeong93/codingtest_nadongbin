import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
plus, minus, product, divide = map(int, sys.stdin.readline().split())

max_num = -1e9
min_num = 1e9

def custom_divide(n1, n2):
    if n1 < 0:
        return -(-n1 // n2)
    return n1 // n2

def dfs(sum, num_idx, plus, minus, product, divide):
    if num_idx == N:
        global max_num, min_num
        max_num = max(max_num, sum)
        min_num = min(min_num, sum)
    
    if plus > 0:
        temp_sum = sum + A[num_idx]
        plus -= 1
        dfs(temp_sum, num_idx+1, plus, minus, product, divide)
        plus += 1
    if minus > 0:
        temp_sum = sum - A[num_idx]
        minus -= 1
        dfs(temp_sum, num_idx+1, plus, minus, product, divide)
        minus += 1
    if product > 0:
        temp_sum = sum * A[num_idx]
        product -= 1
        dfs(temp_sum, num_idx+1, plus, minus, product, divide)
        product += 1
    if divide > 0:
        temp_sum = custom_divide(sum, A[num_idx])
        divide -= 1
        dfs(temp_sum, num_idx+1, plus, minus, product, divide)
        divide += 1

dfs(A[0], 1, plus, minus, product, divide)
print(int(max_num))
print(int(min_num))