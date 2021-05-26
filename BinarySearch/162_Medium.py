"""
2021.05.26
mengfanhui
"""

# 峰值元素是指其值大于左右相邻值的元素。
#
# 给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞ 。

# 思路就是二分法，从中间找。分两种情况，一种 mid > mid + 1说明是下降的趋势，右指针往左移。
# 另一种 mid < mid + 1,上升的趋势，左指针往右移。
# 反正只找到一个就可以了，左右指针相遇的时候就是峰值找到的时候

nums = [1,2,3,1]
# 输出：2
# 解释：3 是峰值元素，你的函数应该返回其索引 2。

class Solution:
    def findPeakElement(self, nums):
        n = nums
        if n == 0:
            return 0
        left = 0
        right = n - 1
        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid
        return left