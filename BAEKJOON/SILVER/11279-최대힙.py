import sys
input = sys.stdin.readline
import heapq
N = int(input())
arr = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(arr) > 0:
            print(-heapq.heappop(arr)[0])
        else:
            print(0)
    else:
        heapq.heappush(arr,(-num,num))
