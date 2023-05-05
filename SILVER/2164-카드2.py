from collections import deque
N = int(input())
q = deque()
for i in range(N):
    q.append(i+1)
while len(q) > 1:
    q.popleft() # 제일 위에 있는 카드 버리기

    num = q.popleft() # 남은 카드 중 제일 위에 있는 카드 꺼내서
    q.append(num) # 제일 아래로 옮기기
print(q.popleft())