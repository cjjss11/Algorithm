from collections import deque
N = int(input())
q = deque()
answer = []
for i in range(N):
    q.append(i+1)
while len(q) > 1: # q에 값이 하나 남을 동안
    ans = q.popleft() # 가장 앞에 있는 숫자 버리고
    answer.append(ans) # answer 리스트에 담기
    num = q.popleft() # 남은 숫자 중에 가장 앞에 있는 숫자를 빼서
    q.append(num) # 가장 뒤로 옮기기
answer.append(q.popleft()) # pop한 순서를 담은 리스트에 가장 마지막에 남은 숫자 append
print(*answer)