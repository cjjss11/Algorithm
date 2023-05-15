# 첫 번째 풀이 방법
import sys
N,S = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
S_sum = 0
end = 0
cnt = 0
minvalue = 21e8
for start in range(N):
    while S_sum < S and end < N:
        S_sum += lst[end]
        end += 1
        cnt += 1 # 하나씩 더할 때 마다 카운트 + 1
    if S_sum >= S:
        if cnt < minvalue:
            minvalue = cnt
        S_sum -= lst[start]
        cnt -= 1 # 하나씩 빼주기
if minvalue == 21e8:
    print(0)
else:
    print(minvalue)


# 두 번째 풀이 방법
import sys
N,S = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
S_sum = 0
end = 0
minvalue = 21e8
for start in range(N):
    while S_sum < S and end < N:
        S_sum += lst[end]
        end += 1
    if S_sum >= S:
        cnt = end - start # end에서 start를 빼준 것이 현재 더해져 있는 개수
        if cnt < minvalue:
            minvalue = cnt
        S_sum -= lst[start]
if minvalue == 21e8:
    print(0)
else:
    print(minvalue)