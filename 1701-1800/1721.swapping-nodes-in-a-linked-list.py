#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# @lc code=start

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        for _ in range(k - 1):
            cur = cur.next
        l = cur

        dh = ListNode(0, head)
        r = dh
        while cur:
            r = r.next
            cur = cur.next

        l.val, r.val = r.val, l.val

        return dh.next


# @lc code=end
