#
# @lc app=leetcode id=971 lang=python3
#
# [971] Flip Binary Tree To Match Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: list[int]) -> list[int]:
        nodes, i, flipped = deque([root]), 0, []
        while nodes:
            node = nodes.pop()
            if not node:
                continue
            if node.val != voyage[i]:
                return [-1]
            i += 1

            if node.left and node.left.val != voyage[i]:
                flipped.append(node.val)
                nodes.append(node.left)
                nodes.append(node.right)
            else:
                nodes.append(node.right)
                nodes.append(node.left)
            
        return flipped


