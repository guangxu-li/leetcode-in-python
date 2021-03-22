#
# @lc app=leetcode id=1178 lang=python3
#
# [1178] Number of Valid Words for Each Puzzle
#

# @lc code=start
from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        words_counter = Counter(
            reduce(lambda mask, ch: mask | 1 << (ord(ch) - ord("a")), word, 0)
            for word in words
        )

        return [
            sum(
                words_counter[combination]
                for combination in reduce(
                    lambda c, ch: c + [m | 1 << (ord(ch) - ord("a")) for m in c],
                    p[1:],
                    [1 << (ord(p[0]) - ord("a"))],
                )
            )
            for p in puzzles
        ]


# @lc code=end
