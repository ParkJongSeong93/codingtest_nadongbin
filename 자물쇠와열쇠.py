# key를 회전시키고 이동시켜서 lock을 모두 채우면 true, 불가능하면 false
# key가 자물쇠를 벗어나도 됨

def rotate90(matrix):
    r_len = len(matrix)
    c_len = len(matrix[0])

    return_matrix = [[0] * r_len for _ in range(c_len)]
    for r in range(r_len):
        for c in range(c_len):
            return_matrix[c][r_len - 1 - r] = matrix[r][c]
    return return_matrix


def solution(key, lock):
    n = len(lock)
    m = len(key)

    # lock이 이미 다 채워져 있으면 True
    if all(all(x == 1 for x in row) for row in lock):
        return True

    # 3n 확장 보드 만들기
    board_size = n * 3
    board = [[0] * board_size for _ in range(board_size)]

    # 중앙에 lock 배치
    for r in range(n):
        for c in range(n):
            board[r + n][c + n] = lock[r][c]

    def check_center():
        # 중앙 n x n이 전부 1이면 성공
        for r in range(n):
            for c in range(n):
                if board[r + n][c + n] != 1:
                    return False
        return True

    # 4번 회전하며 모든 위치에 놓아보기
    cur_key = key
    for _ in range(4):
        cur_key = rotate90(cur_key)

        for x in range(0, n * 2 + 1):      # key의 좌상단 row
            for y in range(0, n * 2 + 1):  # key의 좌상단 col
                # key 올려보기(더하기)
                for i in range(m):
                    for j in range(m):
                        board[x + i][y + j] += cur_key[i][j]

                if check_center():
                    return True

                # 원복(빼기)
                for i in range(m):
                    for j in range(m):
                        board[x + i][y + j] -= cur_key[i][j]

    return False


print(solution([[0,0,0], [1,0,0], [0,1,1]],
               [[1,1,1], [1,1,0], [1,0,1]]))