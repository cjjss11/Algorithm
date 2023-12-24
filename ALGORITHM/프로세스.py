from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    while q:
        maxx = max(q)
        num = q.popleft()
        location -= 1
        if num != maxx:
            q.append(num)
            if location < 0:
                location = len(q)-1
        else:
            answer += 1
            if location < 0:
                break
    return answer