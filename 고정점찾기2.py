import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def find_fixed_point(nums):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid_idx = (start + end) // 2
        mid_val = nums[mid_idx]
        if mid_idx == mid_val:
            return mid_idx
        elif mid_idx < mid_val:
            end = mid_idx - 1
        else:
            start = mid_idx + 1
    return -1

print(find_fixed_point(nums))