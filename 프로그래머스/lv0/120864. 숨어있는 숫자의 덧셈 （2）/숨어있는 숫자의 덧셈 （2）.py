import re
def solution(my_string):
    num_list = list(map(int, re.findall(r'[0-9]+', my_string)))
    
    print(num_list)
    answer = sum(num_list)
    
    return answer

