#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        nodes = deque()
        nodes.append(root)

        avgs = []
        while nodes:
            size = len(nodes)
            sum = 0
            for i in range(size):
                node = nodes.popleft()
                sum += node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

            avgs.append(sum / size)

        return avgs


# @lc code=end
