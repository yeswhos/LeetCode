# 用哈希表记录每个字符（pattern）对应的字符串（str），以及每个字符串（str）对应的字符（pattern）
#
# 即任意一个字符都对应着唯一的字符串，任意一个字符串也只被唯一的一个字符对应。
#
# 也就是需要两个哈希表来记录，一般称为双射

#用例
pattern = "abba"
s = "dog cat cat dog"

#方法
def wordPattern(pattern: str, s: str) -> bool:
    word2ch = {}
    ch2word = {}
    res = list(s.split(" "))
    if len(pattern) != len(res):
        return False
    for ch, word in zip(pattern, res):
        if (ch in word2ch and word2ch[ch] != word) or (word in ch2word and ch2word[word] != ch):
            return False
        word2ch[ch] = word
        ch2word[word] = ch
    return True

print(wordPattern(pattern, s))