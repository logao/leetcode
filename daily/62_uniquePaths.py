# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 问总共有多少条不同的路径？

# 示例 1：
# 输入：m = 3, n = 7
# 输出：28

# 示例
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3
# 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右

# 示例
# 输入：m = 7, n = 3
# 输出：28

# 示例
# 输入：m = 3, n = 3
# 输出：6

# 提示：
# 1 <= m, n <= 100
# 题目数据保证答案小于等于
# 2 * 109
import math


class Solution:
    # 动态规划，定义 F(i,j) 为起点走到该点的距离，能够推断出公式 F(i,j)=F(i-1,j) + F(i,j-1)
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]

    # 组合公式, 理解为 m+n-2 个步骤中选择 选择 m-1 个想下移动的方案数
    # C(m-1 + n-1, m-1), python 中 math.comb 可以直接使用
    def uniquePaths2(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)


print(Solution().uniquePaths(3, 2))
