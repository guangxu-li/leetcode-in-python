#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = dummy_head = ListNode()
        dummy_head.next = head

        while head and head.next:
            while head.next and head.val == head.next.val:
                head = head.next
            
            if prev.next == head:
                prev = head
            else:
                prev.next = head.next
            
            head = head.next
        
        return dummy_head.next
# @lc code=end
