#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = deque([root])
        output = ""
        while nodes and root:
            node = nodes.popleft()
            if not node:
                output += "#"
            else:
                output += str(node.val)
                nodes.append(node.left)
                nodes.append(node.right)
            
            output += " "
        
        return output
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split()
        root = TreeNode(data[0]) if data else None
        nodes = deque([root])
        i = 1
        while i < len(data):
            node = nodes.popleft()
            if not node:
                continue

            node.left = TreeNode(int(data[i])) if data[i] != "#" else None
            nodes.append(node.left)
            i += 1

            node.right = TreeNode(int(data[i])) if data[i] != "#" else None
            nodes.append(node.right)
            i += 1
        
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

