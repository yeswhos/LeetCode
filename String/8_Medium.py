# 字符串转换整数
#
# 四个判断条件：
# "如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。"
# 判断空格
# "假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。"
# "该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。"
# 判断数字
# "假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为[−2 ** 31， 2 ** 31− 1]。如果数值超过这个范围，请返回 INT_MAX (2 ** 31− 1) 或INT_MIN (−2 ** 31) 。
# 判断边界

s = "  -4193 with words"
#expect output -4193

import math
def myAtoi(s):
    n = len(s)
    i = 0
    INT_MAX = int(math.pow(2, 31) - 1)
    INT_MIN = int(math.pow(2, 31)) * (-1)
    res = 0
    flag = 1

    #first
    while (i < n) and (s[i] == " "):
        i += 1
    if n == 0 or i == n:
        return 0

    #second
    if s[i] == "-":
        flag = -1
    if s[i] == "-" or s[i] == "+":
        i += 1

    # Third
    while (i < n) and (s[i].isdigit()):
        res = res * 10 + int(s[i])
        i += 1
        if res > INT_MAX:
            break
    res = res * flag

    #forth
    if res > INT_MAX:
        return INT_MAX
    elif res < INT_MIN:
        return INT_MIN
    else:
        return res

print(myAtoi(s))