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
class Solution:
    def __init__(self):
        self.i = 0;
        
    def str2tree(self, s: str) -> TreeNode:
        if self.i == len(s):
            return None

        val = 0;
        op = 1;
        while self.i < len(s) and s[self.i] != '(' and s[self.i] != ')':
            if s[self.i] == '-':
                op = -1
            else:
                val = val * 10 + int(s[self.i])
            self.i += 1
        root = TreeNode(val * op)
        
        if self.i < len(s) and s[self.i] == '(':
            self.i += 1
            root.left = self.str2tree(s)
        
        if self.i < len(s) and s[self.i] == '(':
            self.i += 1
            root.right = self.str2tree(s)
        
        if self.i < len(s) and s[self.i] == ')':
            self.i += 1
        return root
         
# @lc code=end


