#
# @lc app=leetcode id=1836 lang=python3
#
# [1836] Remove Duplicates From an Unsorted Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        nodes, h = Counter(), head
        while h:
            nodes[h.val] += 1
            h = h.next
        
        dummy_head, h = ListNode(), head
        prev = dummy_head
        dummy_head.next = head

        while h:
            if nodes[h.val] > 1:
                prev.next = h.next
            else:
                prev = h
            
            h = h.next
        
        return dummy_head.next
# @lc code=end
