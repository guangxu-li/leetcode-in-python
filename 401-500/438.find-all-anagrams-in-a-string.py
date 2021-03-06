#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        angrams = []
        counter = Counter(p)

        lo, hi = 0, 0
        cnt = len(p)
        while hi < len(s):
            if hi - lo == len(p):
                if counter[s[lo]] >= 0:
                    cnt += 1
                counter[s[lo]] += 1
                lo += 1

            if counter[s[hi]] >= 1:
                cnt -= 1
            counter[s[hi]] -= 1
            hi += 1

            if not cnt:
                angrams.append(lo)
        
        return angrams


# @lc code=end
