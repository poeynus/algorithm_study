def solution(sizes): # 이거는 왜 안되는 걸까
    answer = sum(sizes, [])
    answer = sorted(answer, reverse=True)
    a = answer[0:len(sizes)]
    b = answer[len(sizes):]
    
    return max(a) * max(b)


def solution(sizes): 
    answer = 0 
    sizes = [sorted(size, reverse=True) for size in sizes] 
    w = [size[0] for size in sizes] 
    h = [size[1] for size in sizes] 
    w, h = max(w), max(h) 
    answer = w * h 
    return answer


# [[60, 50], [30, 70], [60, 30], [80, 40]]	4000
# [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	120
# [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	133

