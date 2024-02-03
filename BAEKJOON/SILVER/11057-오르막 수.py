# 첫 번째 방법 / 뒤 쪽에 숫자 추가

N = int(input())
# dp를 2차 리스트로 초기화
dp = [[0]*10 for _ in range(N+1)]
dp[1] = [1]*10

for i in range(2, N+1):
    for j in range(0, 10):
        dp[i][j] = sum(dp[i-1][j:])

print(sum(dp[N]) % 10007)

# 두 번째 방법 / 앞 쪽에 숫자 추가
N = int(input())
# dp를 1차 리스트에 1로 초기화
dp = [1]*10

for i in range(N-1):
    for j in range(1, 10):
        dp[j] = dp[j] + dp[j-1]
print(sum(dp) % 10007)