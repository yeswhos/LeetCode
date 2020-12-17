# 买股票问题和122问题相似
# 状态转移方程：dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee) (只是这里多了个fee)
#
#             dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
#
# dp[i][0]代表第i天拥有0个股票
#
# 状态转移方程，意思是，第i天有0个股票，有两种情况：
# 一个是第i - 1天就没有股票，一个是第i - 1天有股票，所以是i天的时候给卖了，于是他的利润就是加上卖股票那天的价格，然后再减去手续费
# 还有一个是第i天有一支股票：
# 一个是第i - 1天就有股票，一个是第i - 1天没有股票，所以是第i天购进了股票，于是他的利润要减去买股票的钱
#
# 初始/特殊值：
# 第0天没有买股票，就是0, dp[0][0] = 0
# 第0天有买股票，就是减去第一天股票的价格, dp[0][1] = -price[0]

prices = [1, 3, 2, 8, 4, 9]
fee = 2
#expect output 8

def maxProfit(prices, fee):
    n = len(prices)
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
    return dp[n - 1][0]

print(maxProfit(prices, fee))