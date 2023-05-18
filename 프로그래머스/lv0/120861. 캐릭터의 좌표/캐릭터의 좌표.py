def solution(keyinput, board):
    move = {"up":[0,1], "down":[0, -1], "left": [-1, 0], "right": [1,0] }
    
    pos = (0,0) 
    max_x = board[0]//2
    min_x = - (board[0]//2)
    max_y = board[1]//2
    min_y = - (board[1]//2)
    
    for i in keyinput:
      # print(move[i][0])
        next_x = pos[0] + move[i][0]
        next_y = pos[1] + move[i][1]
        if min_x <= next_x <= max_x and  min_y <= next_y <= max_y:
            pos = [next_x , next_y]
        else:
            pass
        
    answer = pos
    return answer