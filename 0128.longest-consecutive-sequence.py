#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def longest1(nums: List[int]) -> int:
            _max = 0
            dp = {}
            for num in nums: # another option is to build number set first so that we don't need to handle deduplication inside the loop
                if num in dp:
                    continue  # NOTE: ignore duplicates otherwise it might destory the boundary we build.
                lo = dp[num - 1][0] if num - 1 in dp else num
                hi = dp[num + 1][1] if num + 1 in dp else num

                dp[num] = [lo, hi]  # for deduplication
                dp[lo] = [lo, hi]
                dp[hi] = [lo, hi]

                _max = max(_max, hi - lo + 1)

            return _max

        def longest2(nums: List[int]) -> int:
            _max = 0
            nums = set(nums)
            for num in nums:  # iterate the set instead of array to reduce loop cnt
                if num - 1 in nums:
                    continue  # we wanna find the possible sequence start

                val = num
                while val in nums:
                    val += 1
                _max = max(_max, val - num)

            return _max

        # return longest1(nums)
        return longest2(nums)


# @lc code=end
