N = int(input())

cnt=N # 단어 개수
for i in range(N):
  word = input()
  for j in range(0, len(word)-1):
    if word[j]==word[j+1]: 
      # word[j] 에 오는 알파벳이 word[j+1]과 같다면, 즉 알파벳이 연이어서 온다면
      pass
    elif word[j] in word[j+1:]:
      # word[j] 에 오는 알파벳이 word[j+1]에 속한다면 그룹단어가 아님
      cnt-=1 # 
      break
print(cnt)