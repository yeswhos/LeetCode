"""
2021.06.03
mengfanhui
"""

def string_reverse(s, left, right):
    # 相当于指针和递归相结合，当指针相遇或者错过的时候停止
    if left >= right:
        return s
    # 两个两个交换，首先是第0个和最后一个，然后是第一个和倒数第二个
    s[left], s[right] = s[right], s[left]
    # 递归，开始下两个指针
    return string_reverse(s, left+1, right-1)
