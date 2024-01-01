# 조합으로 풀이
L,C = map(int,input().split())
pwd = list(input().split())
for i in range(len(pwd)):
    pwd[i] = ord(pwd[i]) # 정렬하기 위해 아스키 코드로 변환
pwd.sort() # 정렬
for i in range(len(pwd)):
    pwd[i] = chr(pwd[i]) # 다시 문자로 변환
used = [0]*C
path = [0]*L
alpha = ['a','e','i','o','u'] # 모음 리스트
def abc(level,start):
    if level == L:
        vowel = 0  # 모음
        consonant = 0  # 자음
        for i in range(L):
            if path[i] in alpha: # 모음이면
                vowel += 1
            elif path[i] not in alpha: # 자음이면
                consonant += 1
        if vowel >= 1 and consonant >= 2: # 모음이 최소 하나 이상이고 자음이 최소 2개 이상이면
            for i in range(L):
                print(path[i],end='')
            print()
        return
    for i in range(start,C):
        if used[i] == 0:
            path[level] = pwd[i]
            used[i] = 1
            abc(level+1,i+1)
            used[i] = 0
abc(0,0)