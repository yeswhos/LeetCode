# 最大子序列和
#
# 状态转移方程：
# dp[i] = max(nums[i], nums[i] + dp[i - 1])
# 其实就是两种情况，一种是选该元素及之前的元素，就是该元素加上之前选中最大的元素
# 另一种是只选该元素，所以就从该元素开始，重新整理一个数组
#
# 初始状态：
# dp[0] = nums[i]

nums = [-2,1,-3,4,-1,2,1,-5,4]
#expect output 6 (which is [4, -1, 2, 1])

def maxSubArray(nums):
    n = len(nums)
    dp = [[0] for _ in range(n)]
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
    return max(dp)

print(maxSubArray(nums))
