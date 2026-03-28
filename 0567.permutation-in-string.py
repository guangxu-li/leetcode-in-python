#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        base = Counter(s1)
        cur = Counter()
        win_len = len(s1)

        for i in range(len(s2)):
            cur[s2[i]] += 1
            if i >= win_len:
                cur[s2[i - win_len]] -= 1

            if cur == base:
                return True

        return False


# @lc code=end
