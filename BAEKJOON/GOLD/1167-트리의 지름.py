import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v = int(input())
arr = [[] for _ in range(v+1)]
# 각 노드의 연결된 정보를 트리로 표현
for _ in range(v):
    lst = list(map(int,input().split()))
    for i in range(1,len(lst)-2,2):
        arr[lst[0]].append([lst[i],lst[i+1]])
def dfs(y,x):
    # 각 노드와 연결된 노드를 확인
    for a,b in arr[y]:
        # 탐색하지 않은 노드라면
        if used[a] == -1:
            # 탐색하기까지의 걸린 간선의 거리로 초기화
            used[a] = b + x
            dfs(a,b+x)

# 탐색 여부, 간선의 거리
used = [-1]*(v+1)
used[1] = 0
# 1번 노드에서 dfs 탐색
dfs(1,0)

# 1번 노드에서 가장 먼 거리의 노드를 찾음
start = used.index(max(used))
used = [-1]*(v+1)
used[start] = 0
# 1번 노드부터 가장 먼 거리의 노드에서 다시 제일 먼 노드를 찾음
dfs(start,0)

print(max(used))