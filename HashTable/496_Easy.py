"""
2021.05.24
mengfanhui
"""
# 栈加哈希表解决，先用nums2构造一个栈和哈希表，哈希表里面是元素对应其下一个更大值，然后遍历nums1，直接在哈希表找对应的值就可以了

# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
#
# 请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
#
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
#
# 输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出: [-1,3,-1]
# 解释:
#     对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
#     对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
#     对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

def nextGreaterElement(nums1, nums2):
    # 一个栈一个字典
    stack = []
    dic = {}
    # 遍历nums2，找到每个值的右边更大数字
    for num in nums2:
        # 栈不为空，且找到了更大数字的时候，弹出栈顶元素，然后再比较下一个元素
        while len(stack) != 0 and num > stack[-1]:
            temp = stack.pop()
            dic[temp] = num
        # 相当于把更大的数字放入了栈，进行下一次比较
        stack.append(num)
    # 剩下没弹出的都是没有更大的数字，所以赋值-1
    while len(stack) != 0:
        dic[stack.pop()] = -1
    # 把每个nums1的值都放倒字典里，找到对应的值也就是较大数字
    res = []
    for num in nums1:
        res.append(dic[num])
    return res