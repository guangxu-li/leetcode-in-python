#
# @lc app=leetcode id=1814 lang=python3
#
# [1814] Count Nice Pairs in an Array
#

# @lc code=start
from typing import Counter, List


# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# ->
# nums[i] - rev(nums[i]) = nums[j] - rev(nums[j])
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        rev = lambda x: int(str(x)[::-1])

        nums = [num - rev(num) for num in nums]

        cnt, counter = 0, Counter()
        for num in nums:
            cnt = (cnt + counter[num]) % MOD
            counter[num] += 1

        return cnt

# @lc ckde=end
