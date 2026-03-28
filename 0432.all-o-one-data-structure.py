#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#

# @lc code=start
class Node:
    def __init__(self, key: str = "", val: int = 0):
        self.keys, self.val = {key}, val
        self.prev, self.next = None, None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

        self.key_to_node = dict({"": self.head})
        self.val_to_node = dict({0: self.head})
    
    def delete_node(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev
        del self.val_to_node[node.val], node
    
    def insert_behind(self, anchor: Node, key: int, val: int) -> None:
        node, nxt = Node(key, val), anchor.next
        
        anchor.next, node.next = node, nxt
        nxt.prev, node.prev = node, anchor

        self.val_to_node[val] = node

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        cur_node = self.key_to_node.get(key, self.head)
        val = cur_node.val
        cur_node.keys.discard(key)

        if val + 1 not in self.val_to_node:
            self.insert_behind(cur_node, key, val + 1)

        cur_node.next.keys.add(key)
        self.key_to_node[key] = cur_node.next

        if not cur_node.keys:
            self.delete_node(cur_node)
        

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.key_to_node:
            return
        
        cur_node = self.key_to_node[key]
        val = cur_node.val
        cur_node.keys.remove(key)
        del self.key_to_node[key]

        if val - 1:
            if val - 1 not in self.val_to_node:
                self.insert_behind(cur_node.prev, key, val - 1)

            cur_node.prev.keys.add(key)
            self.key_to_node[key] = cur_node.prev
        
        if not cur_node.keys:
            self.delete_node(cur_node)
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return next(iter(self.tail.prev.keys))
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return next(iter(self.head.next.keys))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end


