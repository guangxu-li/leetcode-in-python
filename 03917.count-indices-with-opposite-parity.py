#
# @lc app=leetcode id=3917 lang=python3
#
# [3917] Count Indices With Opposite Parity
#


# @lc code=start
class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        odd = even = 0
        ans = [0] * n

        for i in reversed(range(n)):
            if nums[i] & 1:
                odd += 1
                ans[i] = even
            else:
                even += 1
                ans[i] = odd

        return ans


# @lc code=end
