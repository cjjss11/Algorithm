def solution(s):
    answer = ''
    s_lst = s.split(" ")
    maxx = -21e8
    minn = 21e8
    for i in range(len(s_lst)):
        s_lst[i] = int(s_lst[i])
        if s_lst[i] > maxx:
            maxx = s_lst[i]
        if s_lst[i] < minn:
            minn = s_lst[i]
    maxx = str(maxx)
    minn = str(minn)
    answer += minn
    answer += " "
    answer += maxx
    return answer