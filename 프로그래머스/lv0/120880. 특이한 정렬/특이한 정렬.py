def solution(numlist, n):
    # i-n 크기 순으로 나열하기
    # sorted(<list>, key = <function>, reverse = <bool>)
    # 정렬 기준 1: abs(x-n)
    # 정렬 기준 2: 원래 값인 x의 크기가 큰 순서로 정렬하는 역할 
    # 3과 5 에서 -x 내림차순 
    answer = sorted(numlist, key = lambda x:(abs(x-n),-x)) 
    return answer

