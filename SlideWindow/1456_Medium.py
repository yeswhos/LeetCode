"""
2021.05.27
mengfanhui
"""

# 给你字符串 s 和整数 k 。
#
# 请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
#
# 英文中的 元音字母 为（a, e, i, o, u）。
#
# 也是用滑动窗口，先是直接判断第一次的那一堆里面有几个，
# 然后每次判断去掉的和新增的位置的元素是不是元音字母，从而+-1，然后取最大值
# 然后查找的时候用哈希集合set，因为这样查找快，每个哈希值都对应在哈希表的位置，假如元素存在，查找时间复杂为O（1）
s = "abciiidef"
k = 3
# 输出：3

def maxVowels(self, s: str, k: int) -> int:
    res = 0
    n = len(s)
    vowels_set = set(['a', 'e', 'i', 'o', 'u'])
    for i in range(k):
        if s[i] in vowels_set:
            res += 1
    count = res
    for j in range(k, n):
        if s[j - k] in vowels_set:
            count -= 1
        if s[j] in vowels_set:
            count += 1
    return max(res, count)