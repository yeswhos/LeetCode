"""
2021.05.26
mengfanhui
"""
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。

# 也是用二分，但两个注意的地方，可能要插到最后一个，所以右边那个指针就是长度。
# 然后假如右边指针比target大，那右边放到mid上而不是mid的左边，因为插入的话是插入左边最大小于的右边
nums = [1,3,5,6]
target = 5
# 输出: 2
def searchInsert(self, nums, target):
    n = len(nums)
    left = 0
    right = n
    while left < right:
        mid = left + ((right - left) // 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return left
