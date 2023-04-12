A,B = map(int,input().split())
r_A = []
r_B = []
A = str(A)
B = str(B)
for i in range(len(A)):
    r_A.append(int(A)%10)
    A = int(A)//10
for i in range(len(B)):
    r_B.append(int(B)%10)
    B = int(B)//10

result_A = ''
result_B = ''
for i in range(len(r_A)):
    result_A += str(r_A[i])
for i in range(len(r_B)):
    result_B += str(r_B[i])
if int(result_A) > int(result_B):
    print(result_A)
elif int(result_A) < int(result_B):
    print(result_B)