#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0] * (num + 1)
        
        msb = 1
        while msb <= num:
            for i in range(msb):
                ni = i + msb
                if ni <= num:
                    counter[ni] = 1 + counter[i]
            msb <<= 1

        return counter
# @lc code=end

