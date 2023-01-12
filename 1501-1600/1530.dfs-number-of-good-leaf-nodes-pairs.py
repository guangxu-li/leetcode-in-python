#
# @lc app=leetcode id=1530 lang=python3
#
# [1530] Number of Good Leaf Nodes Pairs
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    # dfs traverse the tree from the bottom to the top
    # returns a list of distances from the leaf node to the parent node of hte current node
    def dfs(self, cur: TreeNode) -> List[int]:
        if not cur:
            return []

        if not cur.left and not cur.right:
            return [1]

        left = self.dfs(cur.left)
        right = self.dfs(cur.right)
        self.count += sum(1 for l in left for r in right if l + r <= self.distance)

        return [n + 1 for n in left + right if n + 1 < self.distance]

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0
        self.dfs(root)

        return self.count


# @lc code=end
