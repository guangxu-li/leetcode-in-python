#
# @lc app=leetcode id=339 lang=python3
#
# [339] Nested List Weight Sum
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
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        nested = deque(nestedList)
        depth = 1
        _sum = 0

        while nested:
            size = len(nested)
            while size:
                size -= 1
                nested_int = nested.popleft()
                if nested_int.isInteger():
                    _sum += depth * nested_int.getInteger()
                else:
                    nested.extend(inner for inner in nested_int.getList())
            depth += 1
        
        return _sum
                
# @lc code=end

