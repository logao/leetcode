from typing import List


# 给定一个二进制数组， 计算其中最大连续1的个数。

# 示例 1:
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

# 注意：
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mxNum = 0
        curNum = 0
        for i, v in enumerate(nums):
            if v == 0:
                curNum = 0
            else:
                curNum += 1
                mxNum = max(curNum, mxNum)
        return mxNum


# test
r = Solution()
print(r.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
