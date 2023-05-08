import sys
input = sys.stdin.readline
import heapq
arr = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(arr) > 0:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr,(abs(num),num)) # 절댓값으로 push
