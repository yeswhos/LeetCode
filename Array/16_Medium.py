# 最接近的三数之和
#
# 利用双指针解题。一般双指针都处理有序数组，而这道题没有要求是连续的三数，所以可以用双指针，一个在i的前一位一个在最后一位。
# 假如三数之和比target大很多，就减小右边指针
# 假如三数之和比target小很多，就增加左边指针

nums = [-1,2,1,-4]
target = 1
#expect output 2    (-1 + 2 + 1 = 2)

def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    res = 0
    distance = float("inf")
    for i in range(n):
        left, right = i + 1, n - 1
        while left < right:
            tmp = nums[i] + nums[left] + nums[right] - target
            if abs(tmp) < distance:
                distance = abs(tmp)
                res = nums[i] + nums[left] + nums[right]
            if tmp > 0:
                right -= 1
            elif tmp < 0:
                left += 1
            else:
                return target
    return res

print(threeSumClosest(nums, target))