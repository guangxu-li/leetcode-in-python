#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
from collections import defaultdict, deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])
        nodes = defaultdict(list)
        min_col = max_col = 0

        while q:
            node, col = q.popleft()
            if not node:
                continue

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            nodes[col].append(node.val)

            q.append((node.left, col - 1))
            q.append((node.right, col + 1))

        return [nodes[col] for col in range(min_col, max_col + 1)]


# @lc code=end
