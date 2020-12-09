from typing import List

# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

# 示例 1:
# 输入: [1,2,3]
# 输出: 6

# 示例 2:
# 输入: [1,2,3,4]
# 输出: 24

# 注意:
#     给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
#     输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。


class Solution:
    # 考虑使用排序后的数组
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        return max(
            nums[l - 1] * nums[l - 2] * nums[l - 3],
            nums[l - 1] * nums[1] * nums[0]
        )

    # ETT
    def maximumProduct2(self, nums: List[int]) -> int:
        tmpMx = nums[0] * nums[1] * nums[2]
        l = len(nums)
        for i in range(l):
            for j in range(1, l):
                for k in range(3, l):
                    if i == j or i == k or j == k: continue
                    tmpMx = max(tmpMx, nums[i] * nums[j] * nums[k])
        return tmpMx


print(Solution().maximumProduct([1, 2, 3,4]))
