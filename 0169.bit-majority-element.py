#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
INT32_SIGN_BIT = 1 << 31
INT32_NEGATIVE_MASK = -1 << 32


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            bit = 1 << i
            cnt = sum(1 if num & bit else 0 for num in nums)
            if cnt > len(nums) // 2:
                ans |= bit

        # (1 << 31) is the int32 sign bit. If it's 1 then it's negative number. But in python no concept of 32-bit int.
        # All negative integer in python have infinite leading 1.
        # So we use -(1 << 32) to get the missing leading ones and combine with the ans to convert it to negative representation.
        # python use two's complement representation

        return ans | INT32_NEGATIVE_MASK if ans & INT32_SIGN_BIT else ans


# @lc code=end
