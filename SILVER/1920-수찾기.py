N = int(input())
N_lst = list(map(int,input().split()))
M = int(input())
M_lst = list(map(int,input().split()))
N_lst.sort()
for i in range(len(M_lst)):
    answer = 0
    st, ed = 0, len(N_lst) - 1
    while st <= ed:
        mid = (st+ed) // 2
        if N_lst[mid] > M_lst[i]:
            ed = mid - 1
        elif N_lst[mid] < M_lst[i]:
            st = mid + 1
        else:
            answer = 1
            break
    print(answer)