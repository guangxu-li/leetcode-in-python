#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        visited, step = set(), 0

        for _, freq in Counter(s).items():
            while freq > 0 and freq in visited:
                freq -= 1
                step += 1
            visited.add(freq)
            
        return step
# @lc code=end
