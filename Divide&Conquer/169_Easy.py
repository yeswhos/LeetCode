"""
2021.06.05
mengfanhui
"""

nums = [2,2,1,1,1,2,2]
def majorityElement(nums):
    # 弄一个递归函数来和分治法解决这个问题
    def getMarjority(left, right):
        # 分治法就是不断分割，直到最小的，也就是只有一个数字的时候。这里最小就是当两个指针走到一起的时候
        if left == right:
            # 返回左右就都一样了，因为只有一个数字
            return nums[left]
        # 分治，找到中间值分开
        mid = left + (right - left) // 2
        # 递归，找左边和右边最大的
        leftMarjority = getMarjority(left, mid)
        rightMarjority = getMarjority(mid+1, right)
        # 如果左右最大的数一样，随便返回一个就行了
        if leftMarjority == rightMarjority:
            return leftMarjority
        # 计数，找两边的最大值
        leftCount, rightCount = 0, 0
        for num in nums:
            if num == leftMarjority:
                leftCount += 1
            if num == rightMarjority:
                rightCount += 1
        return leftMarjority if leftMarjority > rightMarjority else rightMarjority
    return getMarjority(0, len(nums) - 1)

print(majorityElement(nums))