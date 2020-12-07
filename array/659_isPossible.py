# 给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，
# 其中每个子序列都由连续整数组成且长度至少为 3 。
# 如果可以完成上述分割，则返回 true ；否则，返回 false 。
#
# 示例 1：
# 输入: [1,2,3,3,4,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 :
# 1, 2, 3
# 3, 4, 5

# 示例 2：
# 输入: [1,2,3,3,4,4,5,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 :
# 1, 2, 3, 4, 5
# 3, 4, 5

# 示例 3：
# 输入: [1,2,3,4,4,5]
# 输出: False

# 提示：
# 输入的数组长度范围为 [1, 10000]
import heapq
import collections
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = collections.defaultdict(list)
        for x in nums:
            if queue := mp.get(x - 1):
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)
        return not any(queue and queue[0] < 3 for queue in mp.values())

    def isPossible2(self, nums: List[int]) -> bool:
        import collections
        ncr = collections.OrderedDict()  # 将普通字典转换为有序字典
        for i, v in enumerate(nums):
            if len(ncr) == 0:
                ncr[v] = 1
                ncr[v + 1] = 1
            else:
                curReqKey = None
                curReqValue = None
                for k, v in ncr.items():
                    curReqKey = k
                    curReqValue = v
                    break

                if curReqKey == v:
                    curReqValue -= 1
                    if curReqValue == 0:
                        ncr.pop(curReqKey)
                else:
                    ncr[k + 1] = 1 if ncr.get(k + 1) is None else ncr.get(k + 1) + 1
                    ncr[k + 2] = 1 if ncr.get(k + 2) is None else ncr.get(k + 2) + 1

        if len(ncr) > 0:
            return False
        return True


# test
res = Solution()
print(res.isPossible([1, 2, 3, 3, 4, 4, 5, 5]))
