def solution(array, commands):
    answer = []
    for i in commands:
        lst = []
        for j in range(i[0]-1,i[1]):
            lst.append(array[j])
        lst = sorted(lst, key=lambda x:x)
        answer.append(lst[i[2]-1])
    return answer