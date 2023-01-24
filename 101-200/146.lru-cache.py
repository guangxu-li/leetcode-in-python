#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
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

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.dlist = DoubleEndList()
        self.key2node = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        self.dlist.move_to_end(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            node = self.key2node[key]
            node.val = value
            self.dlist.move_to_end(node)

            return

        # new data
        if self.full():
            self.evict()

        node = Node(key, value)
        self.dlist.append(node)
        self.key2node[key] = node

    def evict(self) -> None:
        evicted = self.dlist.popleft()
        del self.key2node[evicted.key]

    def full(self) -> bool:
        return len(self.key2node) == self.capacity


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
