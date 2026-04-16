#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#


# @lc code=start
from typing import Optional


class Node:
    def __init__(self, key: int = 0, val: int = 0, nxt: Optional[Node] = None):
        self.key = key
        self.val = val
        self.nxt = nxt


class TreeNode:
    def __init__(self, key: int = 0, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class LinkedList:
    def __init__(self) -> None:
        self.head = Node()

    def put(self, key: int, val: int) -> None:
        node = self.get_node(key)
        if node:
            node.val = val
            return

        self.head.nxt = Node(key, val, self.head.nxt)

    def get_node(self, key: int) -> Optional[Node]:
        node = self.head.nxt
        while node and node.key != key:
            node = node.nxt
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.val if node else -1

    def remove(self, key: int) -> None:
        prev, curr = self.head, self.head.nxt
        while curr and curr.key != key:
            prev, curr = curr, curr.nxt
        if not curr:
            return
        prev.nxt = curr.nxt


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def predecessor_of(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node or not node.left:
            return None
        node = node.left
        while node.right:
            node = node.right
        return node

    def successor_of(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node or not node.right:
            return None
        node = node.right
        while node.left:
            node = node.left
        return node

    def put(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return

        node = self.root
        while node:
            if node.key < key:
                if not node.right:
                    node.right = TreeNode(key, val)
                node = node.right
            elif node.key > key:
                if not node.left:
                    node.left = TreeNode(key, val)
                node = node.left
            else:
                node.val = val
                return

    def get_node(self, key: int) -> Optional[TreeNode]:
        node = self.root
        while node and node.key != key:
            if node.key < key:
                node = node.right
            else:
                node = node.left
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.val if node else -1

    def remove(self, key: int) -> None:
        parent = None
        node = self.root
        while node and node.key != key:
            parent = node
            if node.key > key:
                node = node.left
            else:
                node = node.right

        predecessor = self.predecessor_of(node)
        if predecessor:
            predecessor.right = node.right
            if parent and parent.left == node:
                parent.left = node.left
            elif parent and parent.right == node:
                parent.right = node.left
            else:
                self.root = node.left
            return

        successor = self.successor_of(node)
        if successor:
            successor.left = node.left
            if parent and parent.left == node:
                parent.left = node.right
            elif parent and parent.right == node:
                parent.right = node.right
            else:
                self.root = node.right
            return

        if parent and parent.left == node:
            parent.left = None
        elif parent and parent.right == node:
            parent.right = None
        else:
            self.root = None


class MyHashMap:
    def __init__(self) -> None:
        self.bucket_num = 749
        # self.buckets = [LinkedList() for _ in range(self.bucket_num)]
        self.buckets = [BinarySearchTree() for _ in range(self.bucket_num)]

    def hash(self, key: int) -> int:
        return key % self.bucket_num

    def put(self, key: int, val: int) -> None:
        self.buckets[self.hash(key)].put(key, val)

    def get(self, key: int) -> int:
        return self.buckets[self.hash(key)].get(key)

    def remove(self, key: int) -> None:
        self.buckets[self.hash(key)].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
