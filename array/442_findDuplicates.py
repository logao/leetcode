# 给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
# 找到所有出现两次的元素。
# 你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
#
# 示例：
# 输入:[4,3,2,7,8,2,3,1]
# 输出:[2,3]
from typing import List

# 测试：考虑边界问题
# 原地修改：使用 -1 做标记时还可以在遍历的过程中记录结果
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for v in nums:
            p = (v - 1) % n
            nums[p] += n
        res = []
        for i, v in enumerate(nums):
            if nums[i] / n > 2:
                res.append(i + 1)
        return res


print(Solution().findDuplicates([1]))
