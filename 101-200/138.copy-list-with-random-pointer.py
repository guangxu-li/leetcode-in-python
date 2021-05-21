#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        h = head
        while h:
            nxt = h.next
            h.next = Node(h.val)
            h.next.next = nxt
            h = nxt
        
        h = head
        while h:
            h.next.random = h.random.next if h.random else None
            h = h.next.next
        
        h = head
        while h:
            nxt = h.next.next
            h.next.next = nxt.next if nxt else None
            h = nxt
        
        return head.next


# @lc code=end
