import sys
from collections import deque

N, A, B = map(int, sys.stdin.readline().split())

one_tiles = list(map(int, sys.stdin.readline().split()))
one_tiles.sort(reverse=True)
one_tiles = deque(one_tiles)
two_tiles = list(map(int, sys.stdin.readline().split()))
two_tiles.sort(reverse=True)
two_tiles = deque(two_tiles)

answer = 0
if N % 2 == 1:
    answer += one_tiles.popleft()
    N -= 1

while N > 0:
    if len(one_tiles) >= 2 and two_tiles:
        if one_tiles[0] + one_tiles[1] > two_tiles[0]:
            answer += one_tiles[0] + one_tiles[1]
            one_tiles.popleft()
            one_tiles.popleft()
        else:
            answer += two_tiles.popleft()

    elif len(one_tiles) >= 2:
        answer += one_tiles[0] + one_tiles[1]
        one_tiles.popleft()
        one_tiles.popleft()

    else:
        answer += two_tiles.popleft()

    N -= 2

print(answer)