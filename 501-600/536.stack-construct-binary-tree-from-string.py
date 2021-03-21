#
# @lc app=leetcode id=536 lang=python3
#
# [536] Construct Binary Tree from String
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
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None

        nodes = deque()
        val, op = None, 1 
        for i in range(len(s)):
            if s[i] == '-':
                op = -1
            elif s[i].isdigit():
                val = val * 10 + int(s[i]) if val else int(s[i])
            elif s[i] == '(':
                if val is not None:
                    nodes.append(TreeNode(val * op))
                val, op = None, 1 
            elif s[i] == ')':
                if val is not None:
                    nodes.append(TreeNode(val * op))
                    val, op = None, 1 

                cur = nodes.pop()
                if not nodes[-1].left:
                    nodes[-1].left = cur
                elif not nodes[-1].right:
                    nodes[-1].right = cur

        return TreeNode(val * op) if val else nodes.pop()
                
# @lc code=end


