# 给定一个整数数组，判断是否存在重复元素。 如果任意一值在数组中出现至少两次，函数返回
# true 。如果数组中每个元素都不相同，则返回 false 。

# 示例
# 输入: [1, 2, 3, 1]
# 输出: true

# 示例
# 输入: [1, 2, 3, 4]
# 输出: false

# 示例
# 输入: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# 输出: true

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(s) != len(nums)


print(Solution().containsDuplicate([1]))
