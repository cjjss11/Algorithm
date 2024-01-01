N,K = map(int,input().split())
girls = [0]*7 # 1학년부터 6학년까지의 여학생 수 담을 리스트 만들기
boys = [0]*7  # 1학년부터 6학년까지의 남학생 수 담을 리스트 만들기
room = 0
for i in range(N):
    S,Y = map(int,input().split())
    if S == 0:  # 성별이 0이면 여학 이므로
        girls[Y] += 1 #  girls 리스트에 해당 학년 인덱스에 1씩 더하기
    elif S == 1: # 성별이 1이면 남학생이므로
        boys[Y] += 1 # boys 리스트에 해당 학년 인덱스에 1씩 더하기
for i in range(7):
    if girls[i] % K == 0: # 해당하는 값을 K로 나눈 나머지가 0이면
        room += girls[i]//K # 해당하는 값을 K로 나눈 몫 만큼 room에 더하기
    else:                
        room += girls[i]//K + 1 # 해당하는 값을 K로 나눈 몫에다가 1 더한 값을 room에 더하기
    if boys[i] % K == 0:
        room += boys[i]//K
    else:
        room += boys[i]//K + 1
print(room)