"""
2021.05.26
mengfanhui
"""

# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

nums = [-1,0,3,5,9,12]
target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4

class Solution:
    def search(self, nums, target) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            # 这样的意思是单纯的左加右除2可能会超过范围
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1