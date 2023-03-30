w,h = map(int,input().split())
N = int(input())
width = [0,w]
height = [0,h]
for i in range(N):
    n1, n2 = map(int,input().split())
    if n1 == 0: # 가로이면
        height.append(n2) # 세로 리스트에 담기
    elif n1 == 1: # 세로이면
        width.append(n2) # 가로 리스트에 담기
width.sort()
height.sort()
maxvalue = -21e8
result = 0
for i in range(len(width)-1):
    for j in range(len(height)-1):
        result = (width[i+1] - width[i]) * (height[j+1] - height[j]) # 넓이 구하기
        if result > maxvalue:
            maxvalue = result
print(maxvalue)