def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

target_idx = binary_search(array, target, 0, len(array)-1)
if target_idx == None:
    print("없는 원소입니다")
else:
    print(f"target index: {target_idx + 1}")
