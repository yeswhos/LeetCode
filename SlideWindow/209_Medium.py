"""
2021.05.27
mengfanhui
"""

# 给定一个含有 n 个正整数的数组和一个正整数
# target 。
#
# 找出该数组中满足其和 ≥ target
# 的长度最小的
# 连续子数组 [numsl, numsl + 1, ..., numsr - 1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回
# 0 。

# 就是滑动窗口，注意下循环中的边界值是否取得到以及是否即使能够跳出循环

target = 15
nums = [1,2,3,4,5]
def minSubArrayLen(target: int, nums) -> int:
    n = len(nums)
    if n == 0:
        return 0
    res = float('inf')
    total, i, j = 0, 0, 0
    while j < n:
        total += nums[j]
        j += 1
        while total >= target:
            res = min(res, j - i)
            total = total - nums[i]
            i += 1

    if res > n:
        return 0
    else:
        return res
print(minSubArrayLen(target, nums))


