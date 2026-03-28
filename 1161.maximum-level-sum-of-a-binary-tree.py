#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        _max = -float("inf")
        ans = level = 1

        while q:
            _sum = sum(q)
            if _max > _sum:
                _max = _sum
                ans = level

            q = [n for node in q for n in [node.left, node.right] if n]
            level += 1

        return ans

# @lc code=end
