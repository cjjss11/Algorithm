import sys
input = sys.stdin.readline
import heapq
arr = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(arr) > 0: # 배열이 비어 있지 않으면
            print(heapq.heappop(arr)[0]) # 가장 작은 값 출력
        else:
            print(0)
    else:
        heapq.heappush(arr,(num,num)) 
