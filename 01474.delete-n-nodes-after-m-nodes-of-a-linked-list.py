#
# @lc app=leetcode id=1474 lang=python3
#
# [1474] Delete N Nodes after M Nodes of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        while cur:
            # keep m
            for _ in range(m - 1):
                if not cur:
                    break
                cur = cur.next

            # delete n
            end = cur
            for _ in range(n + 1):
                if not cur:
                    break
                cur = cur.next

            if end:
                end.next = cur
                cur = end.next

        return head


# @lc code=end
