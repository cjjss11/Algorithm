# 조합 => nCr = n! / (n-r)!r!
n,m = map(int,input().split())
def factorial_n(n): # n!에 대한 계산
    if n == 1:
        return 1
    return n * factorial_n(n-1)
ans_n = factorial_n(n)

r = n-m
def factorial_r(r): # (n-r)!에 대한 계산
    if r == 1: 
        return 1
    return r * factorial_r(r-1)
ans_r = factorial_r(r)

def factorial_m(m): # m!에 대한 계산
    if m == 1:
        return 1
    return m * factorial_m(m-1)
ans_m = factorial_m(m)

result = ans_n // (ans_r*ans_m)
print(result)
