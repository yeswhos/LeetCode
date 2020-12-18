# 不同路径II
#
# 和62比较相似，只不过多了障碍物的限制。
# 如果带用62的代码，会有一些特殊情况的限制，不好处理。
#
# 状态转移方程是一样的，就是加了障碍物的限制
#
# 初始状态视情况而定，主要看起点是不是障碍物
#

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
#expect output 2

def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] != 1:
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    a, b = 0, 0
                    if i != 0:
                        a = dp[i - 1][j]
                    if j != 0:
                        b = dp[i][j - 1]
                    dp[i][j] = a + b
    return dp[m - 1][n - 1]

print(uniquePathsWithObstacles(obstacleGrid))

#12.18 update
#用62的方法解决，运行时间降了很多。

def uniquePathsWithObstacles(obstacleGrid) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        if obstacleGrid[i][0] == 1:
            break
        dp[i][0] = 1
    for j in range(n):
        if obstacleGrid[0][j] == 1:
            break
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] != 1:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = 0
    return dp[-1][-1]

print(uniquePathsWithObstacles(obstacleGrid))