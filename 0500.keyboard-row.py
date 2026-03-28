#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")

        get_row = lambda ch: row1 if ch in row1 else row2 if ch in row2 else row3
        return filter(lambda word: all(ch.lower() in get_row(word[0].lower()) for ch in word), words)

# @lc code=end
