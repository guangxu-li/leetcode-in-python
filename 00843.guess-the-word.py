#
# @lc app=leetcode id=843 lang=python3
#
# [843] Guess the Word
#

# @lc code=start
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
from collections import Counter


class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        #        "acckzz","ccbazz","eiowzz","abcczz"
        # acckzz    6        3        2         3
        # ccbazz    3        6        2         2
        # eiowzz    2        2        6         2
        # abcczz    3        2        2         6

        # 0 a = 2, c = 1, e = 1
        # 1 b = 1, c = 2, i = 1
        # 2 b = 1, c = 2, o = 1
        # 3 a = 1, c = 1, k = 1, w = 1
        # 4 z = 4
        # 5 z = 4

        counters = [Counter(cs) for cs in zip(*words)]
        possibilities = {w: sum(counter[c] for counter, c in zip(counters, w)) for w in words}
        match_count = lambda w1, w2: sum(a == b for a, b in zip(w1, w2))
        while True:
            candidate = max(words, key=possibilities.get)
            if (result := master.guess(candidate)) == 6:
                return
            words = list(filter(lambda w: match_count(candidate, w) == result, words))

# @lc code=end
