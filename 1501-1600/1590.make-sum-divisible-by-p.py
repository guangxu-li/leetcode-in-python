#
# @lc app=leetcode id=1590 lang=python3
#
# [1590] Make Sum Divisible by P
#

# @lc code=start
from itertools import accumulate
from typing import List


# To make the remaining sum divisible by p, then the sum of the target subarray to remove should
# achieve this: `subarray_sum % p = total % p = rem`
#
# It means the candidate solution is defined as following:
#   1. Two prefix_sum[i] and prefix_sum[j] that j <= i
#   2. a = prefix_sum[i] % p, b = prefix_sum[j] % p
#   3. (b - a) % p = total % p = rem
#
# prefix_sum[i] = m * p + a
# prefix_sum[j] = n * p + b
#
# subarray_sum = prefix_sum[j] - prefix_sum[i] = (m - n) * p + (b - a)
# subarray_sum % p = prefix_sum[j] % p - prefix_sum[i] % p = (b - a) % p
#
# Meanwhile:
# subarray_sum % p = rem
#   -> (b - a) % p = rem
#   -> a = (b - rem) % p
#
# That means:
#   Given j that prefix[j] % p = b
#   Find i that prefix[i] % p = (b - rem) % p to form a candidate answer nums[i:j]
# our target: candidate_sum % p = rem -> (v - target) % p = rem -> target = (v - rem) % p
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        pre_sum = list(accumulate(nums, initial=0))
        rem = pre_sum[-1]

        _min = len(nums)
        rem2i = {}
        for i, b in enumerate(pre_sum):
            b %= p
            a = (b - rem) % p

            # we need to put it into the dict first to cover the empty subarray solution.
            # For example: nums: [1], p: 1
            rem2i[b] = i
            if a in rem2i:
                _min = min(_min, i - rem2i[a])

        return _min if _min < len(nums) else -1


# @lc code=end
