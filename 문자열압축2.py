# 문자열 s가 주어질 때 1개 이상 단위로 문자열을 잘라 압축해서 표현할 수 있는 문자열 중 가장 짧은 것의 길이를 return

def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        # 압축된 문자열
        compressed = ""
        # 압축 키워드
        keyword = s[0:step]
        # 압축 카운트
        count = 1

        # 같은 step 만큼 뛰면서 확인
        for j in range(step, len(s), step):
            # 압축 키워드와 매칭해볼 뒷 단어
            rear_word = s[j:step+j]

            # 같다면 카운트 증가
            if rear_word == keyword:
                count += 1
            # 같지 않다면 압축된 문자열에 그대로 저장 혹은 여태 압축된만큼 저장
            else:
                compressed += str(count) + keyword if count >= 2 else keyword
                # 다음 키워드 갱신
                keyword = s[j:j+step]
                # 카운트 초기화
                count = 1
        
        # for문 마지막 부분 압축 처리
        compressed += str(count) + keyword if count >= 2 else keyword
        answer = min(answer, len(compressed))

    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))