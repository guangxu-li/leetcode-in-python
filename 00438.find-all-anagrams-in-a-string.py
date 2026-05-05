#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        target = Counter(p)
        cur = Counter()
        output = []

        for i in range(len(s)):
            cur[s[i]] += 1
            if i >= len(p):
                cur[s[i - len(p)]] -= 1

            if cur == target:
                output.append(i - len(p) + 1)

        return output


# @lc code=end
