#
# @lc app=leetcode id=385 lang=python3
#
# [385] Mini Parser
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack, cur, sign = deque(), None, 1
        for ch in s:
            if ch.isdigit():
                cur = (0 if not cur else cur) * 10 + int(ch)
            elif ch == "-":
                sign = -1
            elif ch == ",":
                if cur is not None:
                    nested_int, cur, sign = NestedInteger(cur * sign), None, 1
                    stack[-1].add(nested_int)
            elif ch == "[":
                stack.append(NestedInteger())
            else:
                if cur is not None:
                    nested_int, cur, sign = NestedInteger(cur * sign), None, 1
                    stack[-1].add(nested_int)
                if len(stack) > 1:
                    popped = stack.pop()
                    stack[-1].add(popped)
        
        return stack.pop() if stack else NestedInteger(cur * sign)

# @lc code=end
