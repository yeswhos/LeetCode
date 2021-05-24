"""
2021.05.24
mengfanhui
"""
# 又是一个方法用集合，判断俩是不是一样就完了
# 给定一个整数数组，判断是否存在重复元素。
#
# 如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

# nums = [1,1,1,3,3,4,3,2,4,2]
# nums = [1, 2, 3, 4]
nums = [3, 1]
def containsDuplicate(nums):
    num_set = set(nums)
    return not sorted(list(num_set)) == sorted(nums)
print(containsDuplicate(nums))