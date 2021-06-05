"""
2021.06.05
mengfanhui
"""
nums = [-2,1,-3,4,-1,2,1,-5,4]
# 这道题就是用的分治法，不过找最大值之和有三种情况，一个是分开左边的最大值，一个是右边的，还有一个是从中间开始往两边扩散的
# 第三种就比较难理解了，专门有个方法是针对这个方法的
def maxSubArray(nums):
    # 判断中间往两边扩的分割的最大值
    def getMidMax(left, right):
        mid = left + (right - left) // 2
        # 两个数，一个是数的综合总和，一个是最大值
        leftSum = nums[mid]
        leftMax = leftSum
        # 遍历数组，从中间往左，看最大值
        for i in range(mid-1, -1, -1):
            leftSum += nums[i]
            leftMax = max(leftSum, leftMax)
        # 和上面一样，只不过这次变成了从中间往右边的最大值
        rightSum = nums[mid+1]
        rightMax = rightSum
        for j in range(mid+2, right, 1):
            rightSum += nums[j]
            rightMax = max(rightMax, rightSum)
        # 左右两个最大值加起来
        return rightMax + leftMax

    # 这个方法就是找最大值，用到递归和分治法，所以可能也是超时的一个原因
    def getMax(left, right):
        # 左右指针相同的时候，说明就分成一个数字就是最小的了，不用再往下分了。
        if left == right:
            return nums[left]
        mid = left + (right - left) // 2
        # 左右中
        leftMax = getMax(left, mid)
        rightMax = getMax(mid+1, right)
        midMax = getMidMax(left, right)
        return max(leftMax, rightMax, midMax)

    return getMax(0, len(nums) - 1)
