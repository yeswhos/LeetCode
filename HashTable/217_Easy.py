"""
2021.05.23
mengfanhui
"""
# 给定一个整数数组，判断是否存在重复元素。
#
# 如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

# nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1, 2, 3, 4]
def containsDuplicate(nums):
    dict = {}
    n = len(set(nums))
    for num in nums:
        if num not in dict.keys():
            dict[num] = 1
        else:
            dict[num] = dict.get(num) + 1
    print(list(dict.values()))
    return list(dict.values()) != [1] * n

print(containsDuplicate(nums))