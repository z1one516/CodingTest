word = input()
word_list = [i.upper() for i in list(map(str, word))]
word_set = list(set(word_list))
word_dict = {}
for i in word_set:
  word_dict[i] = word_list.count(i)

result = [k for k, v in word_dict.items() if v == max(word_dict.values())]
print(result[0] if len(result) == 1 else "?")