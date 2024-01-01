W,H = map(int,input().split())
p,q = map(int,input().split())
t = int(input())
if ((p+t)//W) % 2 == 0:
    x = (p+t) % W
else:
    x = W - ((p+t) % W)
if ((q+t)//H) % 2 == 0:
    y = (q+t) % H
else:
    y = H - ((q+t) % H)
print(x,y)
