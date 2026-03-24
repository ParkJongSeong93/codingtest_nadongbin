# 균형잡힌 괄호 문자열 u, v로 나누기
def divide(s):
    count = 0
    cut_i = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        
        if count == 0:
            cut_i = i
            break
    
    u = s[:cut_i+1]
    v = s[cut_i+1:]
    return u, v

# 올바른 괄호 문자열인지 체크
def check_correct_s(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False
    return True

# dfs를 통해 문제 풀이
def dfs(s):
    # 빈 문자열인 경우
    if s == '':
        return s
    
    # 문자열 분리
    u, v = divide(s)
    if check_correct_s(u):
        # u가 올바른 괄호 문자열이라면
        return u + dfs(v)
    else:
        # u가 올바른 괄호 문자열이 아니라면
        temp = '(' + dfs(v) + ')'
        cut_u = u[1:-1]
        will_be_attached = ''
        for i in range(len(cut_u)):
            if cut_u[i] == '(':
                will_be_attached += ')'
            else:
                will_be_attached += '('
        temp += will_be_attached
        return temp

def solution(p):
    return dfs(p)