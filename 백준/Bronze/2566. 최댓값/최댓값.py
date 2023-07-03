arr = [list(map(int,input().split())) for _ in range(9)]

max = arr[0][0]
max_r = 0
max_c = 0
for i in range(9): # 0~8
  for j in range(9): # 0~8
    if arr[i][j] >= max:
        max = arr[i][j]
        max_r = i
        max_c = j
    else: 
      pass
print(max)
print(max_r+1,max_c+1)
