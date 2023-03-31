#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dh = ListNode(0, head)

        cur = head
        for i in range(n):
            cur = cur.next

        h = dh
        while cur:
            h = h.next
            cur = cur.next

        h.next = h.next.next

        return dh.next


# @lc code=end
