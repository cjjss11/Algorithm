student = int(input())
lst = list(map(int,input().split()))
st_lst = []
for i in range(student):
    st_lst.insert(i-lst[i],i+1)
print(*st_lst)