def solution(today, terms, privacies):
    answer = []
    # 오늘의 날짜를 연도, 월, 일로 나누고 int로 변환
    today_year = int(today[0]+today[1]+today[2]+today[3])
    today_month = int(today[5]+today[6])
    today_day = int(today[8]+today[9])
    
    # 유효기간 담을 딕셔너리
    terms_dic = {}
    for i in terms:
        grade,month = i.split()
        terms_dic[grade] = int(month)
    
    for i in range(len(privacies)):
        date, grade = privacies[i].split()
        year = int(date[0] + date[1] + date[2] + date[3])
        month = int(date[5] + date[6])
        day = int(date[8] + date[9])
        
        # 개인정보 수집 일자에서 월에다가 유효기간을 더함
        month = month + terms_dic[grade]
        # 더했을 때 12배수이면
        if month % 12 == 0:
            # ex) 개인정보 수집 일자 11월이고 유효기간이 13달일 때 더하면 24이므로 
            # 연도가 1 플러스 되고 달은 12월로 되어야 함 
            year = year + ((month//12)-1)
            month = 12
        # 더했을 때 12배수가 아니면
        else:
            if month > 12:
                year = year + (month//12)
                month = month % 12
        
        # 오늘 날짜랑 개인정보 수집 일자를 각각 연도, 월, 일 비교해서 
        # 오늘 날짜가 더 크면 answer에 담기
        if today_year > year:
            answer.append(i+1)
        elif today_year == year:
            if today_month > month:
                answer.append(i+1)
            elif today_month == month:
                if today_day >= day:
                    answer.append(i+1)
        
    return answer