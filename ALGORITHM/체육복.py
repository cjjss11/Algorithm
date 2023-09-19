def solution(n, lost, reserve):
    student = [1] * (n+2)
    
    student[0] = 0
    student[n+1] = 0
    
    for i in reserve:
        student[i] = 2
        
    for i in lost:
        student[i] -= 1
        
    for i in range(1,n+1):
        if student[i] == 0:
            if student[i-1] == 2:
                student[i] = 1
                student[i-1] = 1
            elif student[i+1] == 2:
                student[i] = 1
                student[i+1] = 1
                
    answer = 0
    for i in student:
        if i > 0:
            answer += 1
    return answer