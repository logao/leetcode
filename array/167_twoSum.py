from typing import List


# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

# 说明:
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

# 示例:
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        k = len(numbers)
        for i in range(0, k):
            tmp = target - numbers[i]
            if tmp in numbers[i + 1:]:
                return [i + 1, i + numbers[i + 1:].index(tmp) + 2]
        return []

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        m = dict()
        k = len(numbers)
        for i in range(0, k):
            tmp = target - numbers[i]
            if tmp in m:
                return [m[tmp] + 1, i + 1]
            else:
                m[numbers[i]] = i
        return []

    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        for i, v in enumerate(numbers):
            for j, k in enumerate(numbers[i + 1:]):
                if v + k == target:
                    return [i + 1, i + j + 2]
                if v + k > target:
                    break
        return []


# test
r = Solution()
print(r.twoSum([0,0,3,4], 0))
