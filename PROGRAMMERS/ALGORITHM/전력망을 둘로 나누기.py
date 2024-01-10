from collections import deque

def bfs(start, used, arr):
    q = deque([start])
    result = 1
    used[start] = 1
    while q:
        now = q.popleft()
        for i in arr[now]:
            if used[i] == 0:
                result += 1
                q.append(i)
                used[i] = 1
    return result

def solution(n, wires):
    answer = n
    arr = [[] for _ in range(n+1)]
    for a,b in wires:
        arr[a].append(b)
        arr[b].append(a)
    for a,b in wires:
        used = [0]*(n+1)
        used[b] = 1
        result = bfs(a,used,arr)
        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))
    return answer