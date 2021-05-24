"""
2021.05.24
mengfanhui
"""

# 给定两个字符串 s 和 t，它们只包含小写字母。
#
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
# 请找出在 t 中被添加的字母。

s = "abcd"
t = "abcde"


def findTheDifference(self, s: str, t: str) -> str:
    dic = {}
    for i in s:
        dic[i] = dic.get(i, 0) + 1
    for j in t:
        dic[j] = dic.get(j, 0) - 1
    for key in dic:
        if dic[key] == -1:
            return key
