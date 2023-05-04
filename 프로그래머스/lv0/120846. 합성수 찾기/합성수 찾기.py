# 소수가 아니면 합성수?
# 10 이하 합성수가 아닌 수 : 1,2,3,5,7 > 5
# 10 이하 합성수 : 4, 6, 8, 9, 10 -> 5

# 15 이하 합성수가 아닌 수 : 1,2,3,5,11,13 -> 7
# 15 이하 합성수 :  4, 6, 8, 9, 10, 12, 14, 15 -> 8
import math
def primenumber(x):
    for i in range(2,int(x**0.5+1)):
        if x%i == 0:
            return False # 소수가 아니다     
    return True    



        
def solution(n):
    answer = n-1
    prime_cnt = 0 
    for j in range(2,n+1):# 2 ~ n
        if primenumber(j) == True:
            print(j)
            prime_cnt +=1 
    answer = n - prime_cnt-1
    return answer

solution(10)

