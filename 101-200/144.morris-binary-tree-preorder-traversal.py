#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        curr = root

        while curr:
            if not curr.left:
                output.append(curr.val)
                curr = curr.right
            else:
                last = curr.left
                while last.right and last.right != curr:
                    last = last.right

                if last.right == curr:
                    last.right = None
                    curr = curr.right
                else:
                    last.right = curr
                    output.append(curr.val)
                    curr = curr.left

        return output
# @lc code=end
