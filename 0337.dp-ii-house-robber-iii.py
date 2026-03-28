#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
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
    def rob(self, root: TreeNode) -> int:
        memo = dict({None: [0, 0]})
        nodes = deque()
        node = root

        while nodes or node:
            while node:
                if node.right:
                    nodes.append(node.right)
                nodes.append(node)
                node = node.left

            node = nodes.pop()

            if nodes and node.right == nodes[-1]:
                nodes.pop()
                nodes.append(node)
                node = node.right
            else:
                left = memo[node.left]
                right = memo[node.right]

                memo[node] = [max(left) + max(right), node.val + left[0] + right[0]]
                node = None

        return max(memo[root])


# @lc code=end
