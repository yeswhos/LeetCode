"""
2021.05.26
mengfanhui
"""

# 第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。
#
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
#
# 返回载到每一个人所需的最小船数。(保证每个人都能被船载)。

# 思路就是先排序，最轻的和最重的加起来比较能不能容得下。然后比较第二轻的和第二重的，以此类推

class Solution:
    def numRescueBoats(self, people, limit):
        n = len(people)
        people.sort()
        left = 0
        right = n - 1
        res = 0
        if n == 0:
            return 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            res += 1
        return res