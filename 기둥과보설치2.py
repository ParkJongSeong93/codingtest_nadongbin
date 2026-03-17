# 가능한 조합인지
def possible(built):
    for x, y, a in built:
        # 기둥 
        if a == 0:
            # 바닥 위에 있는 경우, 보의 한쪽 끝 부분 위에 있는 경우, 다른 기둥 위에 있는 경우
            if y == 0 or (x, y-1, 0) in built or (x, y, 1) in built or (x-1, y, 1) in built:
                continue
            return False
        # 보 
        elif a == 1:
            # 한쪽 끝 부분이 기둥 위에 있거나 양쪽 끝 부분이 다른 보와 연결
            if (x, y-1, 0) in built or (x+1, y-1, 0) in built or ((x-1, y, 1) in built and (x+1, y, 1) in built):
                continue
            return False
            
    return True
    

def solution(n, build_frame):
    built = set()    
    for x, y, a, b in build_frame:
        if b == 1:
            built.add((x, y, a))
            if possible(built):
                continue
            else:
                built.remove((x, y, a))
        else:
            if (x, y, a) not in built:
                continue
                
            built.remove((x, y, a))
            if possible(built):
                continue
            else:
                built.add((x, y, a))
    
    return sorted(built)