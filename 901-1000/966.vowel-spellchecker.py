#
# @lc app=leetcode id=966 lang=python3
#
# [966] Vowel Spellchecker
#

# @lc code=start
import re

class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        exact = {w: w for w in wordlist}
        cap = {w.lower(): w for w in reversed(wordlist)}
        devowel = {re.sub("[aeiou]", "#", w.lower()): w for w in reversed(wordlist)}
        # reversed to let first match overwrite others

        # dict.get() return None if key not in dict, but dict[] will throw key error
        # dict.get(key, default) return `default` if key not in dict
        return [
            exact.get(q) or cap.get(q.lower()) or devowel.get(re.sub("[aeiou]", "#", q.lower()), "")
            for q in queries
        ]


# @lc code=end
