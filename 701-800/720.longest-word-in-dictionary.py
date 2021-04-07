#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#

# @lc code=start
from itertools import accumulate


class Solution:
    def longestWord(self, words: list[str]) -> str:
        return min((set(accumulate(w)) - set(words), -len(w), w) for w in words + [""])[2]
# @lc code=end

