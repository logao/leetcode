# 给定两个字符串s和t，它们只包含小写字母。
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 请找出在 t 中被添加的字母。

# 示例
# 输入：s = "abcd", t = "abcde"
# 输出："e"

# 示例
# 输入：s = "", t = "y"
# 输出："y"

# 示例
# 输入：s = "a", t = "aa"
# 输出："a"

# 示例
# 输入：s = "ae", t = "aea"
# 输出："a"

# 提示：
# 0 <= s.length <= 1000
# t.length == s.length + 1
# s 和 t 只包含小写字母

# 總結：
# 字符 <-> 數字：位運算

# Python 強制轉換：
# int(x [,base]) ⇒ 将x转换为一个十进制的整数
# long(x [,base]) ⇒ 将x转换为一个十进制的长整数
# float(x) ⇒ 将x转换为一个浮点数
# str(object) ⇒ 转换为字符串
# repr(object) ⇒ 转换为表达式字符串
# eval(str) ⇒ 用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(seq) ⇒ 将序列seq转换为一个元组
# list(seq) ⇒ 将序列seq转换为一个列表
# chr(x ) ⇒ 将一个整数转换为一个字符
# ord(x ) ⇒ 将一个字符转换为它的整数值
# hex(x ) ⇒ 将一个整数转换为一个十六进制字符串
# oct(x ) ⇒ 将一个整数转换为一个八进制字符串

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ascSum = 0
        for ss, tt in zip(s + chr(0), t):
            ascSum += ord(tt) - ord(ss)
        return chr(abs(ascSum))

    def findTheDifference2(self, s: str, t: str) -> str:
        d = dict()
        for w in s:
            if w not in d:
                d[w] = 1
            else:
                d[w] += 1
        for w in t:
            if w not in d or d[w] == 0:
                return w
            else:
                d[w] -= 1


print(Solution().findTheDifference("ae", "aea"))
