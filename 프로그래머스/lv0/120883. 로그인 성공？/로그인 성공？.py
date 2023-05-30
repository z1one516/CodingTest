def solution(id_pw, db):
    answer = "fail"
    for i in db:
        
        if i[0] == id_pw[0]:
            if i[1] == id_pw[1]:
                answer = "login"
            else:
                answer = "wrong pw"              
    # db에 아이디가 같고 패스워드가 다른 값이 존재한다고 해도 결국 db의 마지막 원소가 id_pw와 다른 값을 가지고 있다면 fail을 반환
    return answer