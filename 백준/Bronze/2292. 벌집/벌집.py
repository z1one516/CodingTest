N = int(input())

end = 1
answer = 0

for i in range(1, N): 
    end += (6*i)
    if end >= N:
        answer = i
        break
print(answer+1) 