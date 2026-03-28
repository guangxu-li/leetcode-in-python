#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            a, b = stack.pop()
            if a == b == None:
                continue
            if a == None or b == None or a.val != b.val:
                return False

            stack.append((a.left, b.left))
            stack.append((a.right, b.right))

        return True


# @lc code=end
