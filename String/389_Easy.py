# 找不同
#
# 虽然是字符串，但是用到了字典以及collection集，
# collections.Counter()返回一个字典类型，统计每个字符出现的次数
# 然后比较次数不同来得出不同的字符

import collections

s = "abcd"
t = "abcde"
#expect output "e"

def findTheDifference(s, t):
    countS = collections.Counter(s)
    countT = collections.Counter(t)
    for val in countT:
        if countT[val] != countS[val]:
            return val

print(findTheDifference(s, t))
