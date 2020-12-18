# 迷路的机器人
#
# 和不同路径62，不同路径II63都很相似，前面都是一样的只不过是把路径打印出来。
#
# 先判断有没有路径能到达，然后反向（从终点到起点）寻找路径，利用dp数组，优先选择可能性多的路径。

obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

#expect output: [[0,0],[0,1],[0,2],[1,2],[2,2]]

def pathWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    res = []
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        return res
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        if obstacleGrid[i][0]:
            break
        dp[i][0] = 1
    for j in range(n):
        if obstacleGrid[0][j]:
            break
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] != 1:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = 0
    if dp[-1][-1] == 0:
        return res
    i, j = m - 1, n - 1
    while i or j:
        res.append([i, j])
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    res.append([i, j])
    res.reverse()
    return res

print(pathWithObstacles(obstacleGrid))