H,M = map(int,input().split())
M = M + (60 - 45)
if M >= 60:
    H = H + 1
    M = M % 60
if H == 0:
    H = 24
H = H - 1
print(f'{H} {M}')