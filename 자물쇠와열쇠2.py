# key를 회전시키고 이동시켜서 lock을 모두 채우면 true, 불가능하면 false
# key가 자물쇠를 벗어나도 됨

def rotate_matrix(key):
    N = len(key)
    rotated_matrix = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            rotated_matrix[r][c] = key[c][N-r-1]
    
    return rotated_matrix

def match_key(key, new_lock, start_r, start_c):
    filled_new_lock = [[0] * len(new_lock) for _ in range(len(new_lock))]
    for r in range(len(new_lock)):
        for c in range(len(new_lock)):
            filled_new_lock[r][c] = new_lock[r][c]

    for r in range(len(key)):
        for c in range(len(key)):
            filled_new_lock[r + start_r][c + start_c] += key[r][c]

    return filled_new_lock

def check_unlocked(filled_new_lock):
    N = len(filled_new_lock)
    for r in range(N // 3, N // 3 * 2):
        for c in range(N // 3, N // 3 * 2):
            if filled_new_lock[r][c] == 1:
                continue
            return False
    return True

def solution(key, lock):
    N = len(lock)

    # 3 * N에 해당하는 자물쇠를 만들고(여백은 빈칸으로) key를 rotate해가며 대조
    new_lock = [[0] * 3*N for _ in range(3*N)]
    for r in range(N, 2*N):
        for c in range(N, 2*N):
            new_lock[r][c] = lock[r-N][c-N]

    for start_r in range(2*N):
        for start_c in range(2*N):
            # key를 rotate하며 넣어보고 new_lock의 가운데 부분이 모두 채워졌는지 확인
            for dir in range(4):
                key = rotate_matrix(key)
                filled_new_lock = match_key(key, new_lock, start_r, start_c)
                unlocked = check_unlocked(filled_new_lock)
                if unlocked:
                    return True

    return False


print(solution([[0,0,0], [1,0,0], [0,1,1]],
               [[1,1,1], [1,1,0], [1,0,1]]))