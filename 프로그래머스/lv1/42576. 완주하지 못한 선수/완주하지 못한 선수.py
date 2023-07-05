def solution(participant, completion):
    people_dict = { i: participant.count(i) for i in participant}
    for i in completion:
        if people_dict[i] == 1:
            del people_dict[i]
        else:
            people_dict[i] -= 1
    answer = list(people_dict.keys())[0]
    return answer 