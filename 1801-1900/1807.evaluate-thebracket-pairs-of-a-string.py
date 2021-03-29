#
# @lc app=leetcode id=1807 lang=python3
#
# [1807] Evaluate the Bracket Pairs of a String
#

# @lc code=start
import re


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = dict(knowledge)
        return re.sub(r"\((\w+?)\)", lambda m: mapping.get(m.group(1), "?"), s)


# @lc code=end
