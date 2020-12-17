# 最长回文子字串
#
# 对于一个回文来说，将他的首位去掉一位之后，他仍然还是会是一个字符串。（条件是长度大于等于2）
# 所以状态转移方程：
# dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
#
# 初始状态，dp中所有相同的单个字符都是回文，所以
# dp[i][i] = True

s = "babad"
#expect output "bab" or "aba"

def longestPalindrome(s: str):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    max_len = 1
    start = 0
    for i in range(n):
        dp[i][i] = True
    for j in range(1, n):
        for i in range(j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False

            if dp[i][j]:
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
    return s[start: start + max_len]

print(longestPalindrome(s))