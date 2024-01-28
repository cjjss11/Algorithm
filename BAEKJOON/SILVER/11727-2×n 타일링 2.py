N = int(input())
dp = [0] * (N+1)
dp[0] = 1
# n==1인 경우 dp[2]를 설정하면 index 오류가 발생
dp[1] = 1

for i in range(2,N+1):
    dp[i] = dp[i-1] * 1 + dp[i-2] * 2

print(dp[N] % 10007)