#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        For the cur window size hi + 1 - lo, the maximum length longest substring that
        satisfies the requirement is 'most_common' + k

        If the window size larger than the maximum length of possible substring then we
        need to shrink the window.

        Otherwise, continue to expand.
        """
        lo, _max, counter, most_common = 0, 0, Counter(), 0
        for hi in range(len(s)):
            counter[s[hi]] += 1
            most_common = max(most_common, counter[s[hi]])
            if hi + 1 - lo > most_common + k:
                counter[s[lo]] -= 1
                lo += 1
            _max = max(_max, hi + 1 - lo)

        return _max


# @lc code=end
