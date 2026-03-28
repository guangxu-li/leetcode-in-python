#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        dp = {0}
        for s in stones:
            dp |= {d + s for d in dp}
        
        _sum = sum(stones)
        return min(abs(_sum - 2 * d) for d in dp)
# @lc code=end
