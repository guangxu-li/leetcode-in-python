#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        @lru_cache(None)
        def is_palindrome(s: str) -> bool:
            left = s[: len(s) // 2]
            right = s[(len(s) + 1) // 2 :]

            return left == right[::-1]

        def dfs(s: str, partitions: List[str]) -> None:
            if not s:
                ans.append(partitions)
                return

            for i in range(1, len(s) + 1):
                cur = s[:i]
                if is_palindrome(cur):
                    dfs(s[i:], partitions + [cur])

        dfs(s, [])
        return ans


# @lc code=end
