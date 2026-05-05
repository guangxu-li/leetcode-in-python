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
    def successor(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node or not node.right:
            return None

        node = node.right
        while node.left:
            node = node.left
        return node

    def predecessor(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node or not node.left:
            return None

        node = node.left
        while node.right:
            node = node.right
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent = None
        node = root
        while node and node.val != key:
            parent = node
            if node.val > key:
                node = node.left
            elif node.val < key:
                node = node.right

        if not node:
            return root

        predecessor = self.predecessor(node)
        if predecessor:
            predecessor.right = node.right
            if parent and parent.left == node:
                parent.left = node.left
                return root
            elif parent and parent.right == node:
                parent.right = node.left
                return root
            else:
                return node.left

        successor = self.successor(node)
        if successor:
            successor.left = node.left
            if parent and parent.left == node:
                parent.left = node.right
                return root
            elif parent and parent.right == node:
                parent.right = node.right
                return root
            else:
                return node.right

        if parent and parent.left == node:
            parent.left = None
            return root
        if parent and parent.right == node:
            parent.right = None
            return root
        else:
            return None


# @lc code=end
