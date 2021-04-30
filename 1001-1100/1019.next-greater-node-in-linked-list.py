#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def nextLargerNodes(self, head: ListNode) -> list[int]:
        stack, ret = deque(), []
        while head:
            while stack and stack[-1][1] < head.val:
                ret[stack.pop()[0]] = head.val
            stack.append((len(ret), head.val))
            ret.append(0)
            head = head.next

        return ret


# @lc code=end
