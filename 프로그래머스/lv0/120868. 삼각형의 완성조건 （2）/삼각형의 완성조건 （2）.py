def solution(sides):
    # [1,2] sum 3 
    # [3,6] sum 9, min 3, max 6 
    ## 나머지 변이 max 일 때 7~8 -> 3개,  6이 max 일 때 4,5,6 -> 2개
    # [11,7] sum 18, min 7, max 11
    ## 나머지 변이 max일 때 12~17 -> 6개, 11이 max일 때 5~11 -> 3개
    answer = sum(sides) - max(sides) + max(sides) - (max(sides)-min(sides)+1)

    return answer