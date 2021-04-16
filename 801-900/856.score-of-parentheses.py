#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        return eval(S.replace(")(", ") + (").replace("()", "1").replace(")", ") * 2"))
# @lc code=end
