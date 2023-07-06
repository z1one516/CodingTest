N, B =input().split() 
sum = 0
for i in range(len(N)): # 0~4 
  if N[i].isalpha() == True:
    sum += (ord(N[i]) - 55)*(int(B)**(len(N)-i-1))
  else:
    sum += int(N[i])*(int(B)**(len(N)-i-1))
    
print(sum)