# 문자열 s가 주어질 때 1개 이상 단위로 문자열을 잘라 압축해서 표현할 수 있는 문자열 중 가장 짧은 것의 길이를 return

def solution(s):
    answer = len(s)

    # 반복되는 길이가 1인 것부터 순차적으로 체크
    for length in range(1, len(s) // 2 + 1):
        keyword = s[0:length]
        compressed = ""
        count = 1

        for j in range(length, len(s), length):
            will_be_matched = s[j:j+length]
            if will_be_matched == keyword:
                count += 1
            else:
                compressed += str(count) + keyword if count >= 2 else keyword
                keyword = will_be_matched
                count = 1
            
        compressed += str(count) + keyword if count >= 2 else keyword
        answer = min(answer, len(compressed))

    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))