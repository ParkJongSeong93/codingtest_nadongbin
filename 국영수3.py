import sys

def main():
    N = int(sys.stdin.readline())
    data = [tuple(map(str, sys.stdin.readline().split())) for _ in range(N)]

    data.sort(key= lambda item : (-int(item[1]), int(item[2]), -int(item[3]), item[0]))
    for item in data:
        print(item[0])

main()