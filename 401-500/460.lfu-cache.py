#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
from collections import defaultdict


class Node:
    def __init__(self, key: int = 0, val: int = 0, freq: int = 0):
        self.key = key
        self.val = val
        self.freq = freq

        self.prev = None
        self.next = None


class DoubleEndList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node: Node) -> None:
        last = self.tail.prev
        last.next = node
        node.next = self.tail

        self.tail.prev = node
        node.prev = last

    def remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def move_to_end(self, node: Node) -> None:
        self.remove(node)
        self.append(node)

    def popleft(self) -> Node:
        if self.empty():
            return None

        node = self.head.next
        self.remove(node)

        return node

    def empty(self) -> bool:
        return self.head.next == self.tail and self.head == self.tail.prev


class LFUCache:
    def __init__(self, capacity: int):
        self.freqs = defaultdict(DoubleEndList)
        self.lf = 0
        self.capacity = capacity
        self.key2node = {}

    def get(self, key: int) -> int:
        if not self.contains(key):
            return -1

        node = self.key2node[key]
        self.count(node)

        return node.val

    def contains(self, key: int) -> bool:
        return key in self.key2node

    def count(self, node: Node) -> None:
        old_freq = node.freq
        new_freq = old_freq + 1
        node.freq = new_freq

        self.freqs[old_freq].remove(node)
        self.freqs[new_freq].append(node)

        if self.freqs[old_freq].empty() and self.lf == old_freq:
            self.lf += 1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None

        if self.contains(key):
            node = self.key2node[key]
            node.val = value
            self.count(node)

            return node.val

        # new data
        if self.full():
            self.evict()

        node = Node(key, value)
        self.key2node[key] = node
        self.freqs[0].append(node)
        self.lf = 0

    def full(self) -> None:
        return len(self.key2node) == self.capacity

    def evict(self) -> None:
        node = self.freqs[self.lf].popleft()
        self.key2node.pop(node.key)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
