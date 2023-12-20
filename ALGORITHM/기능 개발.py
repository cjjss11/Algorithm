from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque()
    for i in range(len(progresses)):
        num = 100 - progresses[i]
        # 100에서 진행률 뺀 값을 속도로 나눈 나머지가 0일 경우
        if num % speeds[i] == 0:
            # 100에서 진행률 뺀 값을 속도로 나눈 몫을 q에 담기
            q.append(num // speeds[i])
        else:
            # 100에서 진행률 뺀 값을 속도로 나눈 나머지가 0이 아닐경우
            # 100에서 진행률 뺀 값을 속도로 나눈 몫에 + 1한 값을 q에 담기
            q.append(num // speeds[i] + 1)
    now = q.popleft()
    result = [now]
    while q:
        next = q.popleft()
        # 다음 값이 현재 값보다 작으면 현재 값이 배포될 때 함께 배포 되므로 
        # 다음 값은 현재 값과 동일한 값으로 인식
        if now > next:
            result.append(now)
        else:
            result.append(next)
            now = next
    result_dic = {}
    for i in result:
        if i not in result_dic:
            result_dic[i] = 1
        else:
            result_dic[i] += 1
    for i in result_dic.values():
        answer.append(i)
    return answer