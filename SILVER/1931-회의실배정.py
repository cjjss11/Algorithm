N = int(input())
lst = []
for _ in range(N):
    st,ed = map(int,input().split())
    lst.append([st,ed])

# 종료 시간 기준으로 정렬 후 만약 같으면 시작 시간 기준으로 정렬
time = sorted(lst, key=lambda x:(x[1],x[0]))
cnt = 1
now = 0
for i in range(1,len(time)):
    if time[now][1] <= time[i][0]:
        now = i
        cnt += 1
print(cnt)
