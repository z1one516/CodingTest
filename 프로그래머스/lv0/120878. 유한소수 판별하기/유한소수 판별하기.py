# 소인수 prime factor : 주어진 자연수를 나누어 떨어뜨리는 약수 중에서 소수인 약수

# 분자, 분모 약분 후 분모 소인수분해 
# 2,5 만 남아있으면 유한 소수

# 최대공약수 
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

# 약분
# for i in range(2,b,1):
#     if a%(i+1) == 0 and b%(i+1) ==0:
#         a = a/(i+1)
#         b = b/(i+1)
        
    
def solution(a, b):
    
    b//= gcd(a,b)
    
    while True:
        if b % 10 == 0: 
            b = b/ 10
        else:  break
        
        
    while True:
        if b%2 ==0:
            b= b/2
        else:  break
    while True: 
        if b%5 ==0:
            b = b/5
        else:  break
    return 1 if b == 1 else 2