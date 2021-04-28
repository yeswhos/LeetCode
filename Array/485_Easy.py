input = [1, 1, 0, 1, 1, 1]

def findMaxConsecutiveOnes(nums):
    count = 0
    result = 0
    n = len(nums)
    if n == 0:
        return 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            result = max(result, count)
            count = 0
    return max(result, count)

print(findMaxConsecutiveOnes(input))