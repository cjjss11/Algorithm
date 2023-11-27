def solution(survey, choices):
    personality = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    choices_dic = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    for i in range(len(survey)):
        if choices[i] < 4:
            cho = choices[i]
            per = survey[i][0]
            personality[per] += choices_dic[cho]
        elif choices[i] > 4:
            cho = choices[i]
            per = survey[i][1]
            personality[per] += choices_dic[cho]

    answer = ''
    first = ['R', 'C', 'J', 'A']
    second = ['T', 'F', 'M', 'N']
    for f,s in zip(first,second):
        if personality[f] < personality[s]:
            answer += s
        elif personality[f] >= personality[s]:
            answer += f
    return answer