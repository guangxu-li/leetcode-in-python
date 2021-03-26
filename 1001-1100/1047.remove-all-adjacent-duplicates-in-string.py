#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
from collections import deque
class Solution:
    def removeDuplicates(self, S: str) -> str:
        chs = deque()
        for ch in S:
            if chs and ch == chs[-1]:
                chs.pop()
            else:
                chs.append(ch)
        
        return "".join(chs)
# @lc code=end

