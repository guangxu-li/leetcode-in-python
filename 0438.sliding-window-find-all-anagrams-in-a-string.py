#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        m, n = len(s), len(p)
        counter, output = Counter(p), []

        lo, hi, k = 0, 0, len(counter)
        while hi < min(m, n):
            if s[hi] in counter:
                if not counter[s[hi]]:
                    k += 1
                counter[s[hi]] -= 1
                if not counter[s[hi]]:
                    k -= 1
            hi += 1
        
        if not k:
            output.append(0)

        while hi < len(s):
            if s[lo] in counter:
                if not counter[s[lo]]:
                    k += 1
                counter[s[lo]] += 1
                if not counter[s[lo]]:
                    k -= 1
            if s[hi] in counter:
                if not counter[s[hi]]:
                    k += 1
                counter[s[hi]] -= 1
                if not counter[s[hi]]:
                    k -= 1

            lo += 1
            hi += 1
            if not k:
                output.append(lo)
        
        return output
# @lc code=end

