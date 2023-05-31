def solution(score):
    answer = []
    mean = []
    
    for i in score:
        mean.append(sum(i)/len(i))
    print(mean)
    sort_list = sorted(mean, reverse = True)
    print(sort_list)
    for i in mean:
        answer.append(sort_list.index(i)+1)

    return answer