#无重复字符的最长子串

# 用双指针的办法，两个都从0出发，如果子串中没有重复，右指针右移
# 如果子串中有重复，左指针右移，直到子串中没有重复元素

s = "abcabcbb"
#expect output 3 (abc)

def lengthOfLongestSubstring(s):
    n = len(s)
    if n <= 1:
        return n
    left, right = 0, 0
    max_len = 0
    while right < n - 1:
        right += 1
        if s[right] not in s[left: right]:
            max_len = max(max_len, right - left + 1)
        else:
            while s[right] in s[left: right]:
                left += 1
    return max_len

print(lengthOfLongestSubstring(s))
