from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        price = q.popleft()
        sec = 0
        # for i in range(len(q))로 하면 시간초과 나는 테케 있음
        for i in q: 
					  # 가격이 떨어지기 전까지 초를 셈
            sec += 1  # 초를 세고
            if price > i:  # 그다음 가격 보다 크면 중
                break
        answer.append(sec)
    return answer