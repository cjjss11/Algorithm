from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    home_y,home_x = map(int,input().split())
    store = []
    for _ in range(n):
        store.append(list(map(int,input().split())))
    festival_y,festival_x = map(int,input().split())
    def bfs():
        q = deque()
        q.append([home_y,home_x])
        used = [0]*n
        while q:
            now = q.popleft()
            now_y,now_x = now[0],now[1]
            if abs(festival_y-now_y) + abs(festival_x-now_x) <= 1000:
                return 'happy'
            for i in range(n):
                if used[i] == 0:
                    store_y,store_x = store[i]
                    if abs(store_y-now_y) + abs(store_x-now_x) <= 1000:
                        q.append([store_y,store_x])
                        used[i] = 1
        return 'sad'
    print(f'{bfs()}')