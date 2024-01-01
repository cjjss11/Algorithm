n = int(input())
num = list(map(int, input().split())) # n개의 숫자가 나열된 수열
max1 = 0 # 최대 연속 증가 횟수
cnt = 0 # 숫자 연속 증가 횟수
for i in range(len(num)-1):
    if num[i+1] >= num[i]:
        cnt += 1 # 숫자 증가하면 연속 증가 횟수 증가
        if cnt > max1: # 최대 증가 횟수 업데이트
            max1 = cnt
    else: # 감소하면 연속 증가 횟수 리셋(최대 증가 횟수 유지)
        cnt = 0

max2 = 0 # 최대 연속 감소 횟수
cnt = 0 # 숫자 연속 감소 횟수
for i in range(len(num)-1):
    if num[i+1] <= num[i]:
        cnt += 1 # 숫자 감소하면 연속 감소 횟수 증가
        if cnt > max2: # 최대 감소 횟수 업데이트
            max2 = cnt
    else: # 증가하면 연속 감소 횟수 리셋(최대 감소 횟수 유지)
        cnt = 0

if max1 > max2:
    print(max1+1)
else:
    print(max2+1)