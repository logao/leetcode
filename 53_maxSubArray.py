from typing import List


# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

class Solution1:  # 动态规划  f(i) = max(f(i-1)+ai,ai)
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        maxAns = nums[0]
        for i, v in enumerate(nums):
            pre = max(pre + v, v)
            maxAns = max(maxAns, pre)
        return maxAns


class Solution2:  # 分治
    def maxSubArray(self, nums: List[int]) -> int:
        maxAns = self.get(nums, 0, len(nums) - 1)[2]
        print(maxAns)
        return maxAns

    def get(self, nums: List[int], l: int, r: int) -> List[int]:
        # return [sl, sr, sm, si]
        # sl: max length for left
        # sr: max length for right
        # sm: max length for whole
        # si: sum for the whole
        if l == r:
            v = nums[l]
            return [v, v, v, v]

        if l < r:
            m = int((l + r) / 2)
            print(l, r, m)
            resL = self.get(nums, l, m)
            resR = self.get(nums, m + 1, r)
            sl = max(resL[0], resL[3] + resR[0])
            sr = max(resR[1], resR[3] + resL[1])
            sm = max(resL[2], resR[2], resL[1] + resR[0])
            si = resL[3] + resR[3]
            return [sl, sr, sm, si]


# test
res = Solution2()
result = res.maxSubArray([-1, 0, -2])
print(result)
