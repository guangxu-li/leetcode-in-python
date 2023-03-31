#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dh = ListNode(0, head)
        end, a, b = dh, head, head.next

        while a and b:
            na, nb = b.next, b.next.next if b.next else None

            end.next = b
            b.next = a
            a.next = None

            end = a
            a, b = na, nb

        if a and not b:
            end.next = a

        return dh.next


# @lc code=end
