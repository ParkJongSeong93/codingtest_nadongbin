# 문자열 s가 주어질 때 1개 이상 단위로 문자열을 잘라 압축해서 표현할 수 있는 문자열 중 가장 짧은 것의 길이를 return

def solution(s):
    answer = len(s)
    n = len(s)

    # i는 자르는 단위
    for i in range(1, n // 2 + 1):
        zipped_str = ""
        a = 0
        while a < n:
            a_list = s[a:a+i]
            count = 1

            b = a + i
            while b < n and s[b:b+i] == a_list:
                count += 1
                b += i

            if count == 1:
                zipped_str += a_list
            else:
                zipped_str += str(count) + a_list

            a = b  # 처리한 만큼 점프

        answer = min(answer, len(zipped_str))

    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))