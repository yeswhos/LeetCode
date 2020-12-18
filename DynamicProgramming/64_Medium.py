# 最小路径和
#
# 和之前的动归，尤其是62，63都相似。
# 状态转移方程：
# dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
# 就是找上一步是从上过来还是从左边过来，值最小
#
# 初始化：
# 沿着边走的都只有一条确定的路线，然后把沿着边走的值都加起来。

grid = [[1,3,1],[1,5,1],[4,2,1]]
#expect output 7

def minPathSum(grid) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]

print(minPathSum(grid))