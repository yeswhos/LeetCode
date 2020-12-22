# Z字形变换
#
# 其实就是一个二维数组的增添，
# 设置两个变量i，flag，一个控制遍历行数的index，一个控制遍历的方向

s = "LEETCODEISHIRING"
numRows = 4
#expect output: "LDREOEIIECIHNTSG"
#Reason as follows:
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G

def convert(s, numRows):
    if numRows < 2:
        return s
    res = ["" for _ in range(numRows)]
    i, flag = 0, -1
    for item in s:
        res[i] += item
        if i == 0 or i == numRows - 1:
            flag = -flag
        i += flag
    return "".join(res)

print(convert(s, numRows))