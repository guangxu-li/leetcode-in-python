#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# Constraints:
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False

        keys = list(pattern)
        words = s.split()

        key2word = {}
        for key, word in zip(keys, words):
            if key not in key2word:
                key2word[key] = word
            elif key2word[key] != word:
                return False

        return len(key2word) == len(set(words))


# @lc code=end
