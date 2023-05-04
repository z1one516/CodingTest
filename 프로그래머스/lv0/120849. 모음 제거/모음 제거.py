def solution(my_string):
    minus = ['a', 'e' , 'i' , 'o', 'u']
    answer = ''
    answer_list = []
    for i in my_string:
        if i not in minus:
            answer_list.append(i)
        
    answer = ''.join(answer_list)
    
    return answer