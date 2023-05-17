def solution(array):
    answer = 0
    arr_list = list(map(str, array))
    for i in arr_list:
        elmnt = list(map(int,i))
        for j in elmnt:
            if j == 7:
                answer +=1
    return answer