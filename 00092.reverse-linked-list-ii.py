#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dhead = ListNode(0)
        dhead.next = head
        prev, cur = dhead, head
        while left > 1:
            prev, cur = cur, cur.next
            left -= 1
            right -= 1

        left_end = prev
        while right:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
            right -= 1

        left_end.next.next = cur
        left_end.next = prev

        return dhead.next

# @lc code=end
