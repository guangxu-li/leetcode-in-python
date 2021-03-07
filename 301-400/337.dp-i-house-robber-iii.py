#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from TreeNode import TreeNode
from typing import List  


class Solution:
    def steal(self, node: TreeNode) -> List[int]:
        if not node:
            return [0, 0]

        left = self.steal(node.left)
        right = self.steal(node.right)

        return [max(left) + max(right), node.val + left[0] + right[0]]

    def rob(self, root: TreeNode) -> int:
        return max(self.steal(root))


# @lc code=end
