#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))

        def cmp(a: str, b: str) -> int:
            ab = a + b
            ba = b + a

            if ab > ba:
                return 1
            elif ab < ba:
                return -1

            return 0

        strs.sort(key=cmp_to_key(cmp), reverse=True)

        return str(int("".join(strs)))


# @lc code=end
