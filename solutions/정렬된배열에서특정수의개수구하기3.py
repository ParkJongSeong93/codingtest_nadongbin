import sys

def main():
    N, x = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))

    def left_search(data, x):
        start = 0
        end = len(data)
        
        while start < end:
            mid = (start + end) // 2
            mid_value = data[mid]
            if mid_value < x:
                start = mid + 1
            else:
                end = mid
        
        return end

    def right_search(data, x):
        start = 0
        end = len(data)

        while start < end:
            mid = (start + end) // 2
            mid_value = data[mid]
            if mid_value <= x:
                start = mid + 1
            else:
                end = mid
        
        return start

    answer = right_search(data, x) - left_search(data, x)
    print(answer if answer > 0 else -1)

main()

# 7 2
# 1 1 2 2 2 2 3