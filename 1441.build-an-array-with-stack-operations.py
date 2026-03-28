#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        ops, i = [], 0
        for j in range(1, target[-1] + 1):
            ops.append("Push")
            if j != target[i]:
                ops.append("Pop")
            else:
                i += 1
        
        return ops

# @lc code=end
