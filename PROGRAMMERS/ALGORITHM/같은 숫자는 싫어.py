# 1. 첫 번째 풀이
from collections import deque
def solution(arr):
    answer = []
    q = deque()
    for i in range(1,len(arr)):  # 첫 번째 요소 제외한 나머지 요소들 q에 담기
        q.append(arr[i])
    now = arr[0]
    answer.append(arr[0])  # 첫 번째 요소는 무조건 포함이므로 답 리스트 담고 시작하기
    while q:
        next = q.popleft()
        if now != next:   # 연속적으로 나타나면 하나 제외하고 모두 지워야 하므로 현재 값이랑 다음 값이 다르면 답 리스트에 담기
            answer.append(next)
        now = next   
    return answer

# 2. 두 번째 풀이
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
            
    return answer