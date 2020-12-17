# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；
# 非负整数 fee 代表了交易股票的手续费用。
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。
# 如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。 返回获得利润的最大值。

# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

# 示例 1:
# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

# 注意:
#     0 < prices.length <= 50000.
#     0 < prices[i] < 50000.
#     0 <= fee < 50000.

from typing import List


# 动态规划：考虑 每天结束后的2种状态，持有股票和不持有股票, 分别记录两种状态下的最大利润
# python: 二元变量赋值时，历史数据先行计算后，再统一赋值给左侧变量名： sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
# python: 初始化数组的方式：rvn = [[0, -prices[0]]] + [[0, 0] for _ in range(l - 1)]

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        l = len(prices)
        rvn = [[0, -prices[0]]] + [[0, 0] for _ in range(l - 1)]
        for i in range(1, l):
            rvn[i][0] = max(rvn[i - 1][0], rvn[i - 1][1] + prices[i] - fee)
            rvn[i][1] = max(rvn[i - 1][1], rvn[i - 1][0] - prices[i])
        return rvn[l - 1][0]

    def maxProfit3(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

    def maxProfit2(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, n):
            sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        return sell


print(Solution().maxProfit([10, 1, 2, 3, 8], 2))
