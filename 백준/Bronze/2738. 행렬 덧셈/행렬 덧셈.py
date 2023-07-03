n, m = map(int,input().split())
matrix_1 = [list(map(int,input().split())) for _ in range(n)]
matrix_2 = [list(map(int,input().split())) for _ in range(n)]

for i in range(m):
  for j in range(n):
    matrix_1[j][i] += matrix_2[j][i]
for i in matrix_1:
  print(*i)