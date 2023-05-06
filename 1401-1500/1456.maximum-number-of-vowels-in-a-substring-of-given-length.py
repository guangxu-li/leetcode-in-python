#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}

        _max = n = 0
        lo = 0
        for hi in range(len(s)):
            if hi - lo >= k:
                n -= s[lo] in vowels
                lo += 1

            n += s[hi] in vowels
            _max = max(_max, n)

        return _max


# @lc code=end
