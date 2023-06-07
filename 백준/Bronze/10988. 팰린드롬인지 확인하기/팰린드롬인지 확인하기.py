check = input()
word = list(map(str,check))
answer = ''

for i in range(len(word)-1,-1,-1):
  answer += word[i]
print(1 if check == answer else 0) 