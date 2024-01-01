def solution(id_list, report, k):
    answer = []
    use_dic = {}    # key는 유저ID, value는 그 유저가 신고한 ID
    report_dic = {} # key는 신고당한ID, value는 신고당한 횟수
    email_dic = {}  # key는 유저ID, value는 k번 이상 신고당한 ID 수
    
    # 딕셔너리 값 채우기
    for i in id_list:
        # 신고당한ID인 value를 리스트로 담기
        use_dic[i] = []
        report_dic[i] = 0
        email_dic[i] = 0
    
    # 한 사람이 한 명만 신고할 수 있기 때문에 한 명을 여러 번 신고한 경우를 제거
    report = list(set(report))
    # 유저ID와 그 유저가 신고한ID 딕셔너리 값 채우기
    for i in report:
        use_id, report_id = i.split()
        use_dic[use_id].append(report_id)

    # 신고당한ID를 확인해서 신고당한 횟수 딕셔너리에 값 채우기
    for value in use_dic.values():
        for i in value:
            report_dic[i] += 1
    
    # k번 이상 신고당한 사람을 찾고 그 사람을 신고한 사람은 메일을 받아야 하므로 
    # email 딕셔너리에 받을 횟수 채우기
    for key,value in report_dic.items():
        if value >= k:
            for keys,values in use_dic.items():
                if key in values:
                    email_dic[keys] += 1
    for key,value in email_dic.items():
        answer.append(value)

    return answer