def solution(array, n):
    answer = 0
    if n not in array: 
        answer = 0
        return answer
    else:
        arr_set = set(array)
        cnt_set = [0]*len(arr_set)

        # print(arr_set)
        # print(cnt_set)
        for i in array:
            for idx, val in enumerate(arr_set):
                if i == val:
                    cnt_set[idx] += 1
        print("cnt_set: ",cnt_set)
        print("arr_set", arr_set)

        for idx, val in enumerate(arr_set):
            if val == n:
                answer = cnt_set[idx]
                return answer
