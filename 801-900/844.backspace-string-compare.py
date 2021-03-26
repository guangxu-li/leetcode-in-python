#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
from typing import Iterable
from itertools import zip_longest


class Solution:
    def traverse(self, s: str) -> Iterable[str]:
        skip = 0
        for ch in reversed(s):
            if ch == "#":
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield ch

    def backspaceCompare(self, S: str, T: str) -> bool:
        return all(
            ch1 == ch2 for ch1, ch2 in zip_longest(self.traverse(S), self.traverse(T))
        )


# @lc code=end
