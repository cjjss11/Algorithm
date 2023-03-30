N = int(input())                                         
lst = [4,3,2,1]                                                                                        
for i in range(N):                                       
    A = list(map(int,input().split()))                   
    B = list(map(int,input().split()))                   
    A_lst = []                                           
    B_lst = []   
    result = 0 
    for i in range(1,len(A)):                            
        A_lst.append(A[i])  # 모양만 따로 리스트에 담음                              
    for i in range(1,len(B)):                            
        B_lst.append(B[i])                               
    for j in range(len(lst)):                                                                
        if A_lst.count(lst[j]) > B_lst.count(lst[j]):  # 카드 수가 A가 더 많으면
            result = 'A'                                 # result에 A 넣기
            break                                        
        elif A_lst.count(lst[j]) < B_lst.count(lst[j]):  # 카드 수가 B가 더 많으면
            result = 'B'                                 # result에 B 넣기
            break  
        elif A_lst.count(lst[j]) == B_lst.count(lst[j]):
            continue
                                                         
    if result == 0:        # result가 0이라는 것은 카드 수가 계속 같았다는 의미                              
        print('D')                                                                                 
    else:                                                
        print(result)