#
# @lc app=leetcode id=1178 lang=python3
#
# [1178] Number of Valid Words for Each Puzzle
#

# @lc code=start
from collections import Counter
from itertools import combinations
from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        words_counter = Counter(frozenset(w) for w in words)

        return [
            sum(
                words_counter[frozenset(c)]
                for k in range(1, 8)
                for c in combinations(p, k)
                if c[0] == p[0]
            )
            for p in puzzles
        ]


# @lc code=end
