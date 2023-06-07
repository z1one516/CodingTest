num_list = list(map(int, input().split()))
chess_list = list(map(int, "1 1 2 2 2 8".split()))

tmp =  [c-n for n, c in zip(num_list, chess_list)]
answer = ' '.join(str(s) for s in tmp)
print(answer)