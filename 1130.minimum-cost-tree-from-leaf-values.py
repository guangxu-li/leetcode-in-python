#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#

# @lc code=start
from collections import deque


class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        """https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space"""
        desc, res = deque([float("inf")]), 0
        for val in arr:
            while desc and desc[-1] <= val:
                _min = desc.pop()
                res += _min * min(val, desc[-1])
            desc.append(val)

        while len(desc) > 2:
            res += desc.pop() * desc[-1]

        return res


# @lc code=end
