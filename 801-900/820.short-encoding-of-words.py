#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#

# @lc code=start
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        codes = set(words)
        for word in words:
            for i in range(1, len(word)):
                codes.discard(word[i:])
        
        return sum(len(code) + 1 for code in codes)
# @lc code=end

