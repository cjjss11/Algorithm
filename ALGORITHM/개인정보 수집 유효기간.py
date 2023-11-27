def solution(today, terms, privacies):
    answer = []
    today_year = int(today[0]+today[1]+today[2]+today[3])
    today_month = int(today[5]+today[6])
    today_day = int(today[8]+today[9])
    terms_dic = {}
    
    for i in terms:
        grade,month = i.split()
        terms_dic[grade] = int(month)
    
    for i in range(len(privacies)):
        date, grade = privacies[i].split()
        year = int(date[0] + date[1] + date[2] + date[3])
        month = int(date[5] + date[6])
        day = int(date[8] + date[9])
        
        month = month + terms_dic[grade]
        if month % 12 == 0:
            year = year + ((month//12)-1)
            month = 12
        else:
            if month > 12:
                year = year + (month//12)
                month = month % 12
            
        if today_year > year:
            answer.append(i+1)
        elif today_year == year:
            if today_month > month:
                answer.append(i+1)
            elif today_month == month:
                if today_day >= day:
                    answer.append(i+1)
        
    return answer