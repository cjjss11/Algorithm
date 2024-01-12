def solution(name):
    # 조이스틱 조작 횟수
    answer = 0
    # 기본 최소 좌우이동 횟수는 길이 - 1
    minn = len(name) - 1
    for i in range(len(name)):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(name[i])-ord('A'),ord('Z')+1-ord(name[i]))
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        minn = min(minn, 2*i+len(name)-next, i+2*(len(name)-next))
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += minn
    return answer