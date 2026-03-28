#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
from typing import List

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0]

        window_size = 1
        cnt = 0
        for i in range(1, num + 1):
            if cnt == window_size:
                cnt = 0
                window_size *= 2
            
            counter.append(1 + counter[i - window_size])
            cnt += 1
        
        return counter

            
        
# @lc code=end

