#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.nodes = defaultdict(list)

    def traversal(self, root: Optional[TreeNode], row: int = 0, col: int = 0) -> None:
        if not root:
            return

        self.min_col = min(self.min_col, col)
        self.max_col = max(self.max_col, col)

        self.nodes[col].append((row, root.val))

        self.traversal(root.left, row + 1, col - 1)
        self.traversal(root.right, row + 1, col + 1)

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        self.min_col = self.max_col = 0
        self.traversal(root)

        return [
            [val for _, val in sorted(self.nodes[col], key=lambda x: x[0])] for col in range(self.min_col, self.max_col + 1)
        ]


# @lc code=end
