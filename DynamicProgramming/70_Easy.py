# 爬楼梯问题
#
# 状态转移方程:dp[i] = dp[i - 1] + dp[i - 2]
# 也就是爬楼梯可以一个台阶一个台阶，也可以两个台阶两个台阶
#
# dp里面存储的是第几节楼梯有几种到达的方式，但比如第i层到达的方式就是第i - 1层的方式 加上 第i - 2层的方式
# 初始状态：
# dp[0] = 1
# dp[1] = 2
# 从第0层表示第1层，也就是第一层只有一种方式，而第二层有两种方式

n = 3
#expect output is 3

def climbStairs(n: int):
    dp = [0] * n
    if n == 1:
        return 1
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n - 1]

print(climbStairs(n))