def solution(p):
    answer = ''

    if p == '':
        return p
    
    def detach(s):
        sum = 0
        u = ''
        v = ''
        for i in range(len(s)):
            if s[i] == '(':
                sum += 1
            elif s[i] == ')':
                sum -= 1
            
            if sum == 0:
                u = s[:i+1]
                v = s[i+1:]
                break
        return u, v
            
    def check_correct(s):
        if s == '':
            return False
        sum = 0
        for i in range(len(s)):
            if s[i] == '(':
                sum += 1
            elif s[i] == ')':
                sum -= 1

            if sum < 0:
                return False
        if sum == 0:
            return True
        return False
    
    def dfs(s):
        if s == '':
            return s
        if check_correct(s):
            return s

        u, v = detach(s)
        if check_correct(u):
            return u + dfs(v)
        else:
            temp = '(' + dfs(v) + ')'
            temp_u = ''
            for i in range(1, len(u)-1):
                if u[i] == '(':
                    temp_u += ')'
                else:
                    temp_u += '('
        
            return temp + temp_u
        
    answer = dfs(p)

    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))