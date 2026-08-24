import sys

N, x = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

def lower_bound(nums, x):
    start, end = 0, len(nums)
    while start < end:
        mid = (start + end) // 2
        if nums[mid] < x:
            start = mid + 1
        else:
            end = mid
    return start

def upper_bound(nums, x):
    start, end = 0, len(nums)
    while start < end:
        mid = (start + end) // 2
        if nums[mid] <= x:
            start = mid + 1
        else:
            end = mid
    return start

count = upper_bound(nums, x) - lower_bound(nums, x)
print(-1 if count == 0 else count)