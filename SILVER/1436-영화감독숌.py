num = 665
idx = 0
N = int(input())
while 1:
    num += 1
    if '666' in str(num):
        idx += 1
    if idx == N:
        print(num)
        break