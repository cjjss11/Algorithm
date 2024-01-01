def solution(n, arr1, arr2):
    answer = []
    new_arr1 = []
    new_arr2 = []
    # 이진수로 변환
    for i in arr1:
        i = bin(i)[2:]
        new_arr1.append(int(i))
        
    for i in arr2:
        i = bin(i)[2:]
        new_arr2.append(int(i))

    # 이진수로 변환한 arr1, arr2를 더하고 문자열로 변환
    sum_arr = [str(new_arr1[i] + new_arr2[i]) for i in range(n)]
    
    for i in range(len(sum_arr)):
        # 길이가 n이 아니면 그 차이 만큼 앞에 0을 붙임
        if len(sum_arr[i]) != n:
            cha = n-len(sum_arr[i])
            sum_arr[i] = (cha*'0')+sum_arr[i]
        new_lst = list(sum_arr[i])
        for j in range(len(new_lst)):
            if new_lst[j] == '0':
                new_lst[j] = ' '
            else:
                new_lst[j] = '#'
        # 리스트로 각각 분리 시켰기 때문에 join으로 합치기
        abc = ''.join(new_lst)
        sum_arr[i] = abc
    
    return sum_arr