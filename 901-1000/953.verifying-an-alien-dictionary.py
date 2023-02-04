#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
from string import ascii_lowercase
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {alien:normal for alien, normal in zip(order, ascii_lowercase)}
        return sorted(words, key=lambda word: str(mapping[ch] for ch in word)) == words

# @lc code=end
