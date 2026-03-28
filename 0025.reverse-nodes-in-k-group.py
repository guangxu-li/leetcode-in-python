#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(root: Optional[ListNode]) -> Optional[ListNode]:
            prev, cur = None, root
            while cur:
                nxt = cur.next
                cur.next = prev
                prev, cur = cur, nxt

            return prev

        dh = ListNode(0, head)

        prev_tail, cur_tail = dh, head
        while cur_tail:
            for _ in range(k - 1):
                if not cur_tail:
                    break
                cur_tail = cur_tail.next

            if not cur_tail:
                break

            cur_head = prev_tail.next
            next_head = cur_tail.next

            cur_tail.next = None
            prev_tail.next = reverse(cur_head)

            cur_head, cur_tail = cur_tail, cur_head
            cur_tail.next = next_head

            prev_tail, cur_tail = cur_tail, next_head
            prev_tail.next = cur_tail

        return dh.next


# @lc code=end
