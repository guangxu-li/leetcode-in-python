#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()
        _max = lo = hi = 0
        while hi < len(s):
            while counter[s[hi]]:
                counter[s[lo]] -= 1
                lo += 1

            counter[s[hi]] += 1
            hi += 1
            _max = max(_max, hi - lo)

        return _max


# @lc code=end
