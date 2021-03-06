#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def __init__(self):
        self.cnt = 0
        self.target = 0
        self.found = defaultdict(int)

    def dfs(self, node: TreeNode, cur: int) -> None:
        if not node:
            return
        
        cur += node.val
        self.cnt += 1 if cur == self.target else 0
        self.cnt += self.found[cur - self.target]

        self.found[cur] += 1
        self.dfs(node.left, cur)
        self.dfs(node.right, cur)
        self.found[cur] -= 1



    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.target = sum
        self.dfs(root, 0)

        return self.cnt
        


# @lc code=end
