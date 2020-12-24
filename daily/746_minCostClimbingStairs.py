# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

# 示例 1:
# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。

# 示例 2:
# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

# 注意：
#     cost 的长度将会在 [2, 1000]。
#     每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
from typing import List


# 解：
# 动态规划：对于滚动数值的定义，初始值的定义需要思考更详细

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cur = pre1 = pre2 = 0
        for x in range(2, n + 1):
            cur = min(pre1 + cost[x - 1], pre2 + cost[x - 2])
            pre2, pre1 = pre1, cur
        return cur

    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        n = len(cost)
        xp2 = cost[0]
        xp1 = cost[1]
        lastStep = 0

        for x in range(2, n):
            oXp2 = xp2
            oXp1 = xp1
            newXp1 = min(
                xp1 + cost[x],
                xp2 + cost[x - 1],
                xp2 + cost[x]
            )
            if newXp1 == xp1 + cost[x]: lastStep = 1
            if newXp1 == xp2 + cost[x - 1]: lastStep = 2
            if newXp1 == xp2 + cost[x]: lastStep = 1

            xp2 = xp1
            xp1 = newXp1
            print(oXp2, oXp1, xp2, xp1)

        if lastStep == 1:
            return xp1
        elif lastStep == 2:
            return xp2
        else:
            min(xp1, xp2)


print(Solution().minCostClimbingStairs( [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
