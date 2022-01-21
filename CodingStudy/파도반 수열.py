n = int(input())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for index in range(0, 98):
    dp[index + 3] = dp[index] + dp[index + 1]

for _ in range(n):
    print(dp[int(input())])
