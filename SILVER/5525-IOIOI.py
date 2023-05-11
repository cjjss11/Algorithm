N = int(input())
M = int(input())
S = list(input())

idx = 1
cnt = 0
pattern = 0
while idx < M-1:
    if S[idx-1] == 'I' and S[idx] == 'O' and S[idx+1] == 'I':
        pattern += 1 # IOI가 한 패턴이므로 존재 여부 찾기
        if pattern == N: #
            cnt += 1
            pattern -= 1
        idx += 1
    else:
        pattern = 0
    idx += 1
print(cnt)
