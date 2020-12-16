# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
#
# 示例1:
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
#
# 示例 2:
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
#
# 示例 3:
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
#
# 示例 4:
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false

# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。

# 题解：哈希表 + 双指针
# python: zip 的使用，同时遍历2个集合

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for ch, word in zip(pattern, words):
            if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
                return False
            word2ch[word] = ch
            ch2word[ch] = word
        return True

    def wordPattern_self(self, pattern: str, s: str) -> bool:
        d = {}
        sl = s.split(' ')
        if len(pattern) != len(sl): return False
        for i, w in enumerate(pattern):
            if w not in d:
                if sl[i] in d.values(): return False
                d[w] = sl[i]
            else:
                if d[w] != sl[i]: return False
        return True


print(Solution().wordPattern('caaa', 'do dog dog dog'))
