#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
import re

class Solution:
    def reverseVowels(self, s: str) -> str:
        return re.sub(r'(?i)[aeiou]', lambda m, v=re.findall(r'(?i)[aeiou]', s): v.pop(), s)
# @lc code=end

