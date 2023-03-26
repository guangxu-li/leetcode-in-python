#
# @lc app=leetcode id=320 lang=python3
#
# [320] Generalized Abbreviation
#

# @lc code=start
from typing import List


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        if not word:
            return [""]

        abbrs = [str(len(word))]
        for i, ch in enumerate(word):
            prev = str(i) if i else ""
            abbrs.extend([prev + ch + nxt for nxt in self.generateAbbreviations(word[i + 1:])])

        return list(abbrs)
# @lc code=end
