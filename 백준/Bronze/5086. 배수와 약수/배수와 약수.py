# baekjoon 5086
while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        break
    elif num2 % num1 == 0:
        print("factor")
    elif num1 % num2 == 0:
        print("multiple")
    else:
        print("neither") 
