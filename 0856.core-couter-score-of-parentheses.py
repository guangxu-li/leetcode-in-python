#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        _sum = depth = 0
        for i, j in zip(S, S[1:]):
            _sum += 1 << depth if i + j == "()" else 0
            depth += 1 if i == "(" else -1
        
        return _sum
# @lc code=end
