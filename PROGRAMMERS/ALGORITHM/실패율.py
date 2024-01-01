def solution(N, stages):
    answer = []
    total = len(stages)
    # set을 활용하여 중복 제거
    set_stages = list(set(stages))
    # 각 스테이지 별 개수 딕셔너리
    stages_dic = {}
    maxvalue = max(set_stages)
    # 실패율 딕셔너리
    fail_rate = {}
    for i in range(1,maxvalue+1):
        stages_dic[i] = 0
        fail_rate[i] = 0
    
    # 각 스테이지 별 개수 값 채우기
    for i in stages:
        stages_dic[i] += 1
    
    for i in range(1,N+1):
        # stage 전체 길이가 0이 아니면
        if total != 0:
            cnt = stages_dic[i]
            fail_rate[i] = cnt / total
            total = total - cnt
        # stage 전체 길이가 0이면
        else:
            fail_rate[i] = 0
            
    # value 기준으로 key 내림차순 정렬
    sorted_stages = sorted(fail_rate.items(), key=lambda x:x[1], reverse=True)

    for i in range(N):
        answer.append(sorted_stages[i][0])

    return answer