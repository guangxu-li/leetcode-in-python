#
# @lc app=leetcode id=320 lang=python3
#
# [320] Generalized Abbreviation
#

# @lc code=start
from typing import List


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def abbr(bitmask: int) -> str:
            w = ""

            cnt = 0
            for i, ch in enumerate(word):
                if bitmask & 1 == 0:
                    cnt += 1
                else:
                    if cnt:
                        w += str(cnt)
                        cnt = 0
                    w += ch

                bitmask >>= 1

            return w + str(cnt) if cnt else w

        return [abbr(bitmask) for bitmask in range(1 << len(word))]
# @lc code=end
