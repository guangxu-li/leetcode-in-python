#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        h = anchor = head
        while h:
            if anchor.val != h.val:
                anchor.next =h 
                anchor =h 
            
            h = h.next
        anchor.next = None
        
        return head
# @lc code=end
