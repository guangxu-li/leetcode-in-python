#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def predecessor(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return None

        node = root.left
        while node.right:
            node = node.right
        return node

    def successor(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.right:
            return None

        node = root.right
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        predecessor = self.predecessor(root)
        if predecessor:
            # root.val = predecessor.val
            # root.left = self.deleteNode(root.left, predecessor.val)
            # return root
            predecessor.right = root.right
            return root.left
        successor = self.successor(root)
        if successor:
            # root.val = successor.val
            # root.right = self.deleteNode(root.right, successor.val)
            # return root
            successor.left = root.left
            return root.right


# @lc code=end
