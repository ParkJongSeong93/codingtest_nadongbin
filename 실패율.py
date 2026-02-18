def solution(N, stages):
    # 각 스테이지에 멈춘 사람 수 세기
    cnt = [0] * (N + 2)  # 1..N, N+1 포함
    for s in stages:
        cnt[s] += 1

    result = []
    reached = len(stages)  # 현재 스테이지에 도달한 사람 수(분모)

    for stage in range(1, N + 1):
        if reached == 0:
            fail = 0
        else:
            fail = cnt[stage] / reached

        result.append((fail, stage))
        reached -= cnt[stage]  # 다음 스테이지 도달자 수로 갱신

    # 실패율 내림차순, 같으면 스테이지 번호 오름차순
    result.sort(key=lambda x: (-x[0], x[1]))

    return [stage for _, stage in result]