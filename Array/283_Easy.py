"""
2021.05.15
mengfanhui
"""
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。

# 用双指针，找出不等于0的放到第一位，剩余的就补充0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        for j in range(index, n):
            nums[j] = 0