# n개의 부품, m개의 부품 확인요청, 숫자순대로 있으면 yes 없으면 no

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
have_array = list(map(int, input().split()))
have_array = sorted(have_array)

m = int(input())
need_array = list(map(int, input().split()))
need_array = sorted(need_array)

for need in need_array:
    target_idx = binary_search(have_array, need, 0, n-1)
    if target_idx == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
    
    # 아래 코드는 시간초과날 수 있음(set을 사용한다면 좋음)
    # if need in have_array:
    #     print("yes", end=" ")
    # else:
    #     print("no", end=" ")