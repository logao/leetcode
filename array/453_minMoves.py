# 给定一个长度为 n 的 非空 整数数组，每次操作将会使 n - 1 个元素增加1。找出让数组所有元素相等的最小操作次数。

# 示例：
# 输入：
# [1, 2, 3]
# 输出： 3
# 解释：
# 只需要3次操作（注意每次操作会增加两个元素的值）：
# [1, 2, 3] = > [2, 3, 3] = > [3, 4, 3] = > [4, 4, 4]

from typing import List


# 数学方法：枚举找规律得出 等式，4 x L - Base = （L - m）*（n-1）

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        m = min(nums)
        s = sum(nums)
        res = s - n * m
        return res


print(Solution().minMoves([2, 0]))
