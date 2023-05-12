N = int(input())
N_lst = list(map(int,input().split()))
M = int(input())
M_lst = list(map(int,input().split()))
N_dic = {}
for i in N_lst:
    if i not in N_dic:
        N_dic[i] = 1
    else:
        N_dic[i] += 1
for i in range(M):
    if M_lst[i] in N_dic:
        a = M_lst[i]
        print(N_dic[a],end=' ')
    else:
        print(0,end=' ')
