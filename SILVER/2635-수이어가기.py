N = int(input())
maxvalue = -21e8
num = 0
for i in range(1,N+1):
    lst = [N] # N값을 미리 넣고 값 담을 리스트 만들기
    result = 0
    n = 1
    lst.append(i)
    while result > -1:
        for j in range(n,len(lst)):
            result = lst[j-1] - lst[j] #앞의 앞의 수에서 앞의 수를 뺀 값
            if result > -1:
                lst.append(result) # 뺀 값이 양수이면 리스트에 담기
                n += 1
            else:
                break
    if len(lst) > maxvalue: # 리스트 안에 원소 개수가 maxvalue 보다 크면
        maxvalue = len(lst) # maxvalue 갱신
        num = i # lst 원소 개수가 최대일 때 두번째 값 갱신
print(maxvalue)
answer = [N,num]
for i in range(2,maxvalue):
    answer.append(answer[i-2]-answer[i-1])
print(*answer)