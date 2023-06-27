# baekjoon 2941
word = input()
subtract = ["c=", "c-","dz=", "d-", "lj", "nj", "s=", "z="] 

# word count
subtract_count = 0
for i in subtract:
  subtract_count += word.count(i)
      
# print("subtract_count: ", subtract_count)
answer = len(word) - subtract_count
print(answer)