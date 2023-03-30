lst = []
for i in range(9):
    num = int(input())
    lst.append(num) # 난쟁이의 키를 하나의 리스트로 만들기
sum = 0
sum2 = 0
for i in range(9):
    sum += lst[i] # 9명의 난쟁이 키 합 구하기
sum2 = sum - 100  # 9명의 난쟁이 키 합에서 100 빼기
flag = 0
for i in range(8):
    a = lst[i]
    for j in range(i+1,9):
        b = lst[j]
        if a + b == sum2: # 두개씩 더해서 sum2와 같으면 break
            lst.remove(a)
            lst.remove(b)
            flag = 1
            break
    if flag:
        break
for i in range(len(lst)-1):  # 선택정렬
    for j in range(i+1,len(lst)):
        if lst[i] > lst[j]:
            lst[i],lst[j] = lst[j],lst[i]
for i in lst:
    print(i)