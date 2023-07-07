def solution(arr):
    answer = [10]
    for i in range(len(arr)):
        p = arr.pop()

        if answer[len(answer)-1] != p:
            answer.append(p)
    answer.pop(0)
    answer.reverse()
    return answer