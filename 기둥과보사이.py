# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나 다른 기둥 위
# 보는 한쪽 끝 부분이 기둥 위에 있거나 양쪽 끝이 다른 보와 연결, 바닥은 안됨

# 전체를 돌면서 가능한 구조인지 확인
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥
            if y == 0:
                continue
            if [x, y-1, 0] in answer:
                continue
            if [x, y, 1] in answer or [x-1, y, 1] in answer:
                continue
            return False

        else:  # 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                continue
            if [x-1, y, 1] in answer and [x+1, y, 1] in answer:
                continue
            return False

    return True


def solution(n, build_frame):
    answer = []

    for x, y, stuff, operate in build_frame:
        if operate == 0:  # delete
            if [x, y, stuff] in answer:
                answer.remove([x, y, stuff])
                if not possible(answer):
                    answer.append([x, y, stuff])

        else:  # install
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])

    return sorted(answer)