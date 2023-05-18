def solution(dots):
    # dots unique x좌표, y좌표 모으기
    # x 좌표 : 각 원소의 첫 번째
    x_list = [dots[i][0] for i in range(4) ]
        
    # y 좌표 : 각 원소의 두 번째
    y_list = [ dots[i][1] for i in range(4) ]
    
    height = max(y_list) - min(y_list)
    length = max(x_list) - min(x_list)
    
    answer = height * length
    return answer