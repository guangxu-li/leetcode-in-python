#
# @lc app=leetcode id=325 lang=python3
#
# [325] Maximum Size Subarray Sum Equals k
#

# @lc code=start
from itertools import accumulate
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        visited = {0: 0}

        _max = 0
        for i, sum_before in enumerate(accumulate(nums, initial=0)):
            target = sum_before - k
            if target in visited:
                _max = max(_max, i - visited[target])
            if sum_before not in visited:
                visited[sum_before] = i

        return _max
# @lc code=end
