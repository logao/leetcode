# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

# 示例 1:
# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释:
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.

# 示例 2:
# 输入: [1,2,2,3,1,4,2]
# 输出: 6

# 注意:
#     nums.length 在1到50,000区间范围内。
#     nums[i] 是一个在0到49,999范围内的整数。

from typing import List

# 哈希表，第一次遍历的过程中存储信息
# python：三个变量的初始化
# python: dict.get 的默认值

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(right[x] - left[x] + 1, ans)
        return ans

    def findShortestSubArray2(self, nums: List[int]) -> int:
        maxD = 0
        minL = len(nums)
        n = []
        d = dict()
        l = dict()
        r = dict()

        for ii, i in enumerate(nums):
            if d.__contains__(i):
                d[i] += 1
                r[i] = ii
            else:
                d[i] = 1
                l[i] = ii
                r[i] = ii
            if maxD == d[i]:
                n.append(i)
            if maxD < d[i]:
                maxD = d[i]
                n.clear()
                n.append(i)
        for i in n:
            ln = r[i] - l[i] + 1
            minL = min(ln, minL)
        return minL


print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
