def solution(n):
    i = 0 # i 3진법

    for j in range(n):# j 10진법
        i += 1
        # print(i)
        while i%3 ==0 or '3' in str(i): 
            i += 1
        # print("3의저주 : ", i)
    
    answer = i
    return answer