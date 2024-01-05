def solution(answers):
    answer = []
    # 규칙 찾기
    lst1 = [1,2,3,4,5]
    lst2 = [2,1,2,3,2,4,2,5]
    lst3 = [3,3,1,1,2,2,4,4,5,5]
    # 최대 10000문제이므로 그만큼 채우기
    answer1 = lst1*(10000//len(lst1))
    answer2 = lst2*((10000//len(lst2))+1)
    answer3 = lst3*((10000//len(lst3))+1)
    cnt1,cnt2,cnt3 = 0,0,0
    # 답안이랑 같으면 카운트
    for i in range(len(answers)):
        if answers[i] == answer1[i]:
            cnt1 += 1
        if answers[i] == answer2[i]:
            cnt2 += 1
        if answers[i] == answer3[i]:
            cnt3 += 1
            
    maxx = [cnt1,cnt2,cnt3]
    maxvalue = max(maxx)
    # 최댓값 찾고 그 최댓값이랑 같으면 답 넣기
    for i in range(3):
        if maxx[i] == maxvalue:
            answer.append(i+1)
    
    return answer