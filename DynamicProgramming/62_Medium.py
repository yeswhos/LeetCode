# 不同路径
#
# 和爬楼梯大同小异，都是每一步的上一步都有两种情况，一个是在左边一个是在上边（机器人只能往右或者下移动）
#
# 状态转移方程：
# dp[i] = dp[i - 1][j] + dp[i][j - 1]
#
# 初始状态：贴边的格子都是只有一种情况
# dp[m][0] = 1
# dp[0][n] = 1

m = 3
n = 7
#expect output 28

def uniquePaths(m, n):
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

print(uniquePaths(m, n))