#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
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
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            root = TreeNode(v, root)
            
        nodes = deque()
        nodes.append(root)
        depth = 1 
        while nodes:
            size = len(nodes)
            while size > 0:
                size -= 1
                node = nodes.popleft()
                
                if not node:
                    continue

                if depth == d - 1:
                    node.left = TreeNode(v, node.left)
                    node.right = TreeNode(v, None,node.right)
                else:
                    nodes.append(node.left)
                    nodes.append(node.right)
            
            depth += 1
        
        return root
# @lc code=end

