# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
#
# 示例
# 输入: [1, 2, 0]
# 输出: 3
#
# 示例
# 输入: [3, 4, -1, 1]
# 输出: 2
#
# 示例
# 输入: [7, 8, 9, 11, 12]
# 输出: 1
#
# 提示：
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。

from typing import List


# 哈希：数组 + abs + 正负号，可以做成简易的 哈希表 携带布尔信息
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            nums[i] = l + 1 if nums[i] <= 0 else nums[i]
        for x in nums:
            if l >= abs(x) >= 1:
                nums[abs(x) - 1] = -1 * abs(nums[abs(x) - 1])
        for i in range(l):
            if nums[i] > 0:
                return i + 1
        return l + 1


print(Solution().firstMissingPositive([3, 4, -1, 1]))
