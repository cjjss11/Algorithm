import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N)]
lst = list(map(int,input().split()))
node = int(input())
for i in range(1,N):
    arr[lst[i]].append(i)

def dfs(now):
    lst[now] = -2
    # 전체 트리 노드 반복
    for i in range(N):
        # 지우고자 하는 노드 now와 lst[i]가 같으면
        # now의 자식이라는 의미이므로 자식도 같이 지워야 함
        if now == lst[i]:
            dfs(i)
cnt = 0
# 지워야 하는 노드로 탐색
dfs(node)
# 지운 노드들을 -2로 체크 했기 때문에 -2가 아니고 지워야 하는 노드가 트리 노드에 있지 않다면
for i in range(N):
    if lst[i] != -2 and i not in lst:
        cnt += 1
print(cnt)