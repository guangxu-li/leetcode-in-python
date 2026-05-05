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
from collections import deque


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodes, cnt = deque([(root, root.val)]), 0

        while nodes:
            node, _max = nodes.popleft()
            if not node:
                continue
            
            if node.val >= _max:
                _max = node.val
                cnt += 1
            
            nodes.append((node.left, _max))
            nodes.append((node.right, _max))
        
        return cnt
            
# @lc code=end

