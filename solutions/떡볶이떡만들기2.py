import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    tteoks = list(map(int, sys.stdin.readline().split()))

    start = 0
    end = max(tteoks)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        len_sum = 0
        for tteok in tteoks:
            if tteok > mid:
                len_sum += tteok - mid
        
        if len_sum >= M:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    print(result)

main()