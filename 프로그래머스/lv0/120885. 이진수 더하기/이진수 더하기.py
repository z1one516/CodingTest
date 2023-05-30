def solution(bin1, bin2):
    
    bin1= list(map(int, bin1))
    bin2= list(map(int, bin2))    

    num1 = 0
    num2 = 0
    
    for idx, val in enumerate(bin1):
        num1 += 2**(len(bin1)-idx-1)*val
    # print(num1)   
    for idx, val in enumerate(bin2):
        num2 += 2**(len(bin2)-idx-1)*val        
    # print(num2)   
    num = num1+num2
    # print(num)
    
    answer = "".join(list(str(bin(num)))[2:])

    return answer