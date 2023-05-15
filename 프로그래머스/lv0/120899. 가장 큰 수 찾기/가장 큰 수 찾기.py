def solution(array):
    answer = [ ]
    for idx, value in enumerate(array):
        if value == max(array):
            answer.append(value)
            answer.append(idx)     
    return answer