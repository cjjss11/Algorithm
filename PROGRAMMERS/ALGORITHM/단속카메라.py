def solution(routes):
    # 필요한 카메라 수
    answer = 0
    # 진출 시점 기준으로 오름차순
    routes.sort(key=lambda x:x[1])
    # 제한 사항에 -30000 이상이라고 하였으므로
    key = -30001
    
    for route in routes:
        # 기준(카메라)보다 진입지점이 뒤에 있으면
        if route[0] > key:
            # 단속이 필요하므로 카메라 하나 추가
            answer += 1
            # 새로운 기준은 해당 경로의 진출지점(맨끝)
            key = route[1]
            
    return answer