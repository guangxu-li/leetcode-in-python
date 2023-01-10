#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        output = []

        while stack or root:
            # for a single subproblem (root), always do this first
            while root:
                stack.append(root.right)
                stack.append(root)  # root is popped first
                root = root.left

            node = stack.pop()
            if not node:
                continue

            if stack and node.right == stack[-1]:
                root = stack.pop()  # new subproblem
                stack.append(node)  # exchange the order
            else:
                output.append(node.val)

        return output


# @lc code=end
