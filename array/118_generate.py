from typing import List


#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        r1 = [1]
        r2 = [1, 1]
        if numRows <= 0:
            return []
        elif numRows == 1:
            return [r1]
        elif numRows == 2:
            return [r1, r2]
        else:
            res.append(r1)
            res.append(r2)
            for i in range(2, numRows):
                row = [1]
                for j in range(1, i):
                    a = res[i - 1][j - 1]
                    b = res[i - 1][j]
                    row.append(a + b)
                row.append(1)
                res.append(row)
            return res


# test
res = Solution()
print(res.generate(6))
