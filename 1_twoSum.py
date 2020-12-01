from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print(type(nums))
        for i, i_n in enumerate(nums):
            for j, j_n in enumerate(nums):
                if i == j:
                    continue
                if (i_n + j_n) == target:
                    return [i, j]


# test
res = Solution()
print(res.twoSum([1, 2, 3, 4], 3))
