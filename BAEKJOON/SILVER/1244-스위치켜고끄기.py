N = int(input())
switch = list(map(int,input().split()))
student = int(input())
for i in range(student):
    gene,num = map(int,input().split())
    if gene == 1:
        for j in range(N):
            if (j+1) % num == 0:
                if switch[j] == 0:
                    switch[j] = 1
                elif switch[j] == 1:
                    switch[j] = 0
    elif gene == 2:
        num2 = num-1
        if switch[num2] == 0:
            switch[num2] = 1
        elif switch[num2] == 1:
            switch[num2] = 0
        plus = 1
        while 1:
            if 0 <= num2-plus and num2+plus < len(switch) and switch[num2-plus] == switch[num2+plus]:
                if switch[num2-plus] == 0:
                    switch[num2-plus] = 1
                elif switch[num2-plus] == 1:
                    switch[num2-plus] = 0
                if switch[num2+plus] == 0:
                    switch[num2+plus] = 1
                elif switch[num2+plus] == 1:
                    switch[num2+plus] = 0
                plus += 1
            else:
                break
for i in range(0,len(switch),20):
    print(*switch[i:i+20])