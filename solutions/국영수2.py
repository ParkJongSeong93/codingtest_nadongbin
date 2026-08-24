import sys

N = int(sys.stdin.readline())
scores = [tuple(sys.stdin.readline().split()) for _ in range(N)]

scores.sort(key= lambda item : (-int(item[1]), int(item[2]), -int(item[3]), item[0]))
for item in scores:
    print(item[0])