"""
2021.06.03
mengfanhui
"""

# 递归解法，在leetcode是不会通过的，时间复杂度太高，但也是个解题的思路

def fib(self, n: int) -> int:
    def fib_cur(n):
        if n < 2:
            return n
        return fib_cur(n - 1) + fib_cur(n - 2)

    return fib_cur(n)