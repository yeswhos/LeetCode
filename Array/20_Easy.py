"""
2021.05.23
mengfanhui
"""

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。

s = "{[]}"
def isValid(s: str) -> bool:
    n = len(s)
    if n % 2 != 0:
        return False
    stack = []
    for obj in s:
        # 遇到左括号就放
        if obj in ["(", "{", "["]:
            stack.append(obj)
        else:
            if len(stack) == 0:
                return False
            # 遇到右括号就弹，然后比较弹的。栈先进后出
            tmp = stack.pop()
            if obj == ")" and tmp != "(":
                return False
            elif obj == "]" and tmp != "[":
                return False
            elif obj == "}" and tmp != "{":
                return False
    return len(stack) == 0
print(isValid(s))