# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 返回锯齿形层序遍历如下：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 树：广度优先遍历
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = [root]
        l2r = False
        while queue:
            l2r = not l2r
            tmpQueue = []
            res.append([])
            l = len(res)
            for item in queue:
                res[l - 1].append(item.val)

                if l2r:
                    if item.left:
                        tmpQueue.append(item.left)
                    if item.right:
                        tmpQueue.append(item.right)
                else:
                    if item.right:
                        tmpQueue.append(item.right)
                    if item.left:
                        tmpQueue.append(item.left)

            tmpQueue.reverse()
            queue = tmpQueue
        return res


r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
# r.left.right = TreeNode(5)
# r.right.left = TreeNode(15)
r.right.right = TreeNode(5)

print(Solution().zigzagLevelOrder(r))
