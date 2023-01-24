#
# @lc app=leetcode id=277 lang=python3
#
# [277] Find The Celebrity
#

# @lc code=start
from functools import lru_cache

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# 1. find the celebrity candidate
# 2. verify the candidate
#
# Let's say the candidate is 0 at the beginning, and we go through from 1 to n - 1.
# There will be two cases:
#   1. candidate knows i -> the candidate is not the celebrity, and i is the candidate now
#   2. candidate doesn't knows i -> i is not the celebrity.
#
# So in the end, we can always have a single one celebrity candidate.
class Solution:
    @lru_cache(None)
    def knows(self, a, b: int) -> bool:
        return knows(a, b)

    def findCelebrity(self, n: int) -> int:
        candi = 0
        for i in range(n):
            if self.knows(candi, i):
                candi = i

        for i in range(n):
            if i == candi:
                continue
            if self.knows(candi, i) or not self.knows(i, candi):
                return -1

        return candi


# @lc code=end
