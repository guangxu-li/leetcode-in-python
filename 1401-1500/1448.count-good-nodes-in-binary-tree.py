#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, _max: float = float("-inf")) -> int:
        return (
            self.goodNodes(root.left, max(_max, root.val))
            + self.goodNodes(root.right, max(_max, root.val))
            + (root.val >= _max)
            if root
            else 0
        )


# @lc code=end
