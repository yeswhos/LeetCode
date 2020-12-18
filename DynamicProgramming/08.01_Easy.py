# 三步问题
#
# 和爬楼梯一样，只不过有两个不同，一个是增加了一种可能性是一次爬三层
# 一个是规定了边界，不能超过int的范围1000000007，所以得结果的时候要对结果取模
#
# 状态转移方程：
# dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
#
# 初始状态：
# dp[0] = 1
# dp[1] = 2
# dp[2] = 4
# 同样的，0代表一层，以此类推

n = 5
#expect output 13

def waysToStep(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3, n):
        dp[i] = (dp[i - 1] + (dp[i - 2] + dp[i - 3]) % 1000000007) % 1000000007
    return dp[n - 1]

print(waysToStep(n))