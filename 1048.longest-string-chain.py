#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        counter = defaultdict(int)

        for word in sorted(words, key=len):
            counter[word] = max([counter[word[:i] + word[i + 1 :]] + 1 for i in range(len(word))])

        return max(counter.values())


# @lc code=end
