#
# @lc app=leetcode id=1363 lang=python3
#
# [1363] Largest Multiple of Three
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        num_str = lambda ds: str(int("".join(map(str, ds)))) if ds else ""

        digits.sort(reverse=True)
        rem = sum(digits) % 3  # 0 1 2
        if rem == 0:
            return num_str(digits)

        rem2digits = defaultdict(list)
        for d in digits:
            rem2digits[d % 3].append(d)

        # rem == 1 -> remove 1xone or 2xtwo
        # rem == 2 -> remove 1xtwo or 2xone
        a, b = rem2digits[1], rem2digits[2]
        if rem == 2:
            a, b = b, a

        if a:
            digits.remove(a[-1])
        elif len(b) >= 2:
            digits.remove(b[-1])
            digits.remove(b[-2])
        else:
            return ""

        return num_str(digits)


# @lc code=end
