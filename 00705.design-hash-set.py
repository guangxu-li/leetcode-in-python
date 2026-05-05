#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#


# @lc code=start
class Node:
    def __init__(self, val: int = 0, prev: Node = None, nxt: Node = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.nxt = self.tail
        self.tail.prev = self.head

    def add(self, val: int):
        if self.contains(val):
            return
        node = Node(val, self.head, self.head.nxt)
        self.head.nxt = node
        node.nxt.prev = node

    def remove(self, val: int):
        prev = self.head
        curr = self.head.nxt
        while curr != self.tail:
            if curr.val == val:
                prev.nxt = curr.nxt
                curr.nxt.prev = prev
                break
            prev = curr
            curr = curr.nxt

    def contains(self, val: int) -> bool:
        prev = self.head
        curr = self.head.nxt
        while curr != self.tail:
            if curr.val == val:
                return True
            curr = curr.nxt

        return False


class BinarySearchTree:
    def __init__(self):
        self.tree = None

    def predecessor(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node or not node.left:
            return None
        node = node.left
        while node.right:
            node = node.right
        return node

    def successor(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node or not node.right:
            return None
        node = node.right
        while node.left:
            node = node.left
        return node

    def add(self, val: int):
        if not self.tree:
            self.tree = TreeNode(val)
            return

        node = self.tree
        while node:
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                    return
                node = node.right
            elif node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    return
                node = node.left
            else:
                return

    def remove(self, val: int):
        parent = None
        node = self.tree
        while node and node.val != val:
            parent = node
            if node.val < val:
                node = node.right
            else:
                node = node.left

        if not node:
            return

        predecessor = self.predecessor(node)
        if predecessor:
            predecessor.right = node.right
            if parent and parent.left == node:
                parent.left = node.left
            elif parent and parent.right == node:
                parent.right = node.left
            else:
                self.tree = node.left
            return

        successor = self.successor(node)
        if successor:
            successor.left = node.left
            if parent and parent.left == node:
                parent.left = node.right
            elif parent and parent.right == node:
                parent.right = node.right
            else:
                self.tree = node.right
            return

        # node is a leaf node
        if parent and parent.left == node:
            parent.left = None
        elif parent and parent.right == node:
            parent.right = None
        else:
            self.tree = None

    def contains(self, val: int) -> bool:
        node = self.tree
        while node:
            if node.val < val:
                node = node.right
            elif node.val > val:
                node = node.left
            else:
                return True
        return False


class MyHashSet:

    def __init__(self):
        self.bucket_num = 769
        # self.buckets = [DoublyLinkedList() for _ in range(self.bucket_num)]
        self.buckets = [BinarySearchTree() for _ in range(self.bucket_num)]

    def hash(self, key: int):
        return key % self.bucket_num

    def add(self, key: int) -> None:
        return self.buckets[self.hash(key)].add(key)

    def remove(self, key: int) -> None:
        return self.buckets[self.hash(key)].remove(key)

    def contains(self, key: int) -> bool:
        return self.buckets[self.hash(key)].contains(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
