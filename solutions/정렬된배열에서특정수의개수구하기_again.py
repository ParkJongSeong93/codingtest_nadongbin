import sys

def main():
    input = sys.stdin.readline
    N, x = map(int, input().split())
    arr = list(map(int, input().split()))

    # 왼쪽의 인덱스 찾기
    def find_left():
        start = 0
        end = len(arr)
        while start < end:
            mid = (start + end) // 2
            # 중간값이 target보다 작을 때
            if arr[mid] < x:
                start = mid + 1
            # 중간값이 target보다 크거나 같을 때
            elif arr[mid] >= x:
                end = mid
        return start

    # target 이상이 나오는 인덱스
    def find_right():
        start = 0
        end = len(arr)
        while start < end:
            mid = (start + end) // 2
            if arr[mid] <= x:
                start = mid + 1
            elif arr[mid] > x:
                end = mid
        return start

    print(find_right() - find_left() if find_right() - find_left() != 0 else -1)

main()