#
# @lc app=leetcode id=1578 lang=python3
#
# [1578] Minimum Deletion Cost to Avoid Repeating Letters
#

# @lc code=start
class Solution:
    def minCost(self, s: str, cost: list[int]) -> int:
        hi, anchor, total_cost, _max, _cost = 0, s[0], 0, 0, 0

        while hi < len(s):
            if s[hi] == anchor:
                total_cost += cost[hi]
                _max = max(_max, cost[hi])
                hi += 1
            else:
                _cost += total_cost - _max
                anchor, total_cost, _max = s[hi], 0, 0

        return _cost + total_cost - _max

                


# @lc code=end

